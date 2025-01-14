import gradio as gr
import torch
import spaces
from PIL import Image
import os
from transformers import CLIPTokenizer, CLIPTextModel, AutoProcessor, T5EncoderModel, T5TokenizerFast
from diffusers import AutoencoderKL, FlowMatchEulerDiscreteScheduler
from flux.transformer_flux import FluxTransformer2DModel
from flux.pipeline_flux_chameleon import FluxPipeline
import torch.nn as nn
import math
import logging
import sys
from qwen2_vl.modeling_qwen2_vl import Qwen2VLSimplifiedModel
from huggingface_hub import snapshot_download

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

MODEL_ID = "Djrango/Qwen2vl-Flux"
MODEL_CACHE_DIR = "model_cache"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE = torch.bfloat16

# Aspect ratio options
ASPECT_RATIOS = {
    "1:1": (1024, 1024),
    "16:9": (1344, 768),
    "9:16": (768, 1344),
    "2.4:1": (1536, 640),
    "3:4": (896, 1152),
    "4:3": (1152, 896),
}

class Qwen2Connector(nn.Module):
    def __init__(self, input_dim=3584, output_dim=4096):
        super().__init__()
        self.linear = nn.Linear(input_dim, output_dim)
    
    def forward(self, x):
        return self.linear(x)

# Download models if not present
if not os.path.exists(MODEL_CACHE_DIR):
    logger.info("Starting model download...")
    try:
        snapshot_download(
            repo_id=MODEL_ID,
            local_dir=MODEL_CACHE_DIR,
            local_dir_use_symlinks=False
        )
        logger.info("Model download completed successfully")
    except Exception as e:
        logger.error(f"Error downloading models: {str(e)}")
        raise

# Initialize models in global context
logger.info("Starting model loading...")

# Load smaller models to GPU
tokenizer = CLIPTokenizer.from_pretrained(os.path.join(MODEL_CACHE_DIR, "flux/tokenizer"))
text_encoder = CLIPTextModel.from_pretrained(
    os.path.join(MODEL_CACHE_DIR, "flux/text_encoder")
).to(DTYPE).to(DEVICE)

text_encoder_two = T5EncoderModel.from_pretrained(
    os.path.join(MODEL_CACHE_DIR, "flux/text_encoder_2")
).to(DTYPE).to(DEVICE)

tokenizer_two = T5TokenizerFast.from_pretrained(
    os.path.join(MODEL_CACHE_DIR, "flux/tokenizer_2")
)

# Load larger models to CPU
vae = AutoencoderKL.from_pretrained(
    os.path.join(MODEL_CACHE_DIR, "flux/vae")
).to(DTYPE).cpu()

transformer = FluxTransformer2DModel.from_pretrained(
    os.path.join(MODEL_CACHE_DIR, "flux/transformer")
).to(DTYPE).cpu()

scheduler = FlowMatchEulerDiscreteScheduler.from_pretrained(
    os.path.join(MODEL_CACHE_DIR, "flux/scheduler"),
    shift=1
)

# Load Qwen2VL to CPU
qwen2vl = Qwen2VLSimplifiedModel.from_pretrained(
    os.path.join(MODEL_CACHE_DIR, "qwen2-vl")
).to(DTYPE).cpu()

# Load connector and embedder
connector = Qwen2Connector().to(DTYPE).cpu()
connector_path = os.path.join(MODEL_CACHE_DIR, "qwen2-vl/connector.pt")
connector_state = torch.load(connector_path, map_location='cpu')
connector_state = {k.replace('module.', ''): v.to(DTYPE) for k, v in connector_state.items()}
connector.load_state_dict(connector_state)

t5_context_embedder = nn.Linear(4096, 3072).to(DTYPE).cpu()
t5_embedder_path = os.path.join(MODEL_CACHE_DIR, "qwen2-vl/t5_embedder.pt")
t5_embedder_state = torch.load(t5_embedder_path, map_location='cpu')
t5_embedder_state = {k: v.to(DTYPE) for k, v in t5_embedder_state.items()}
t5_context_embedder.load_state_dict(t5_embedder_state)

# Set all models to eval mode
for model in [text_encoder, text_encoder_two, vae, transformer, qwen2vl, connector, t5_context_embedder]:
    model.requires_grad_(False)
    model.eval()

logger.info("All models loaded successfully")

# Initialize processors and pipeline
qwen2vl_processor = AutoProcessor.from_pretrained(
    MODEL_ID,
    subfolder="qwen2-vl",
    min_pixels=256*28*28,
    max_pixels=256*28*28
)

pipeline = FluxPipeline(
    transformer=transformer,
    scheduler=scheduler,
    vae=vae,
    text_encoder=text_encoder,
    tokenizer=tokenizer,
)

def process_image(image):
    """Process image with Qwen2VL model"""
    try:
        # Move Qwen2VL models to GPU
        logger.info("Moving Qwen2VL models to GPU...")
        qwen2vl.to(DEVICE)
        connector.to(DEVICE)
        
        message = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": "Describe this image."},
                ]
            }
        ]
        text = qwen2vl_processor.apply_chat_template(
            message, 
            tokenize=False, 
            add_generation_prompt=True
        )

        with torch.no_grad():
            inputs = qwen2vl_processor(
                text=[text], 
                images=[image], 
                padding=True, 
                return_tensors="pt"
            ).to(DEVICE)
            
            output_hidden_state, image_token_mask, image_grid_thw = qwen2vl(**inputs)
            image_hidden_state = output_hidden_state[image_token_mask].view(1, -1, output_hidden_state.size(-1))
            image_hidden_state = connector(image_hidden_state)
            
            result = (image_hidden_state.cpu(), image_grid_thw)
        
        # Move models back to CPU
        qwen2vl.cpu()
        connector.cpu()
        torch.cuda.empty_cache()
        
        return result
            
    except Exception as e:
        logger.error(f"Error in process_image: {str(e)}")
        raise

def resize_image(img, max_pixels=1050000):
    if not isinstance(img, Image.Image):
        img = Image.fromarray(img)
    
    width, height = img.size
    num_pixels = width * height
    
    if num_pixels > max_pixels:
        scale = math.sqrt(max_pixels / num_pixels)
        new_width = int(width * scale)
        new_height = int(height * scale)
        new_width = new_width - (new_width % 8)
        new_height = new_height - (new_height % 8)
        img = img.resize((new_width, new_height), Image.LANCZOS)
    
    return img

def compute_t5_text_embeddings(prompt):
    """Compute T5 embeddings for text prompt"""
    if prompt == "":
        return None
        
    text_inputs = tokenizer_two(
        prompt,
        padding="max_length",
        max_length=256,
        truncation=True,
        return_tensors="pt"
    ).to(DEVICE)
    
    prompt_embeds = text_encoder_two(text_inputs.input_ids)[0]
    prompt_embeds = t5_context_embedder.to(DEVICE)(prompt_embeds)
    t5_context_embedder.cpu()
    
    return prompt_embeds

def compute_text_embeddings(prompt=""):
    with torch.no_grad():
        text_inputs = tokenizer(
            prompt,
            padding="max_length",
            max_length=77,
            truncation=True,
            return_tensors="pt"
        ).to(DEVICE)

        prompt_embeds = text_encoder(
            text_inputs.input_ids,
            output_hidden_states=False
        )
        pooled_prompt_embeds = prompt_embeds.pooler_output
        return pooled_prompt_embeds

@spaces.GPU(duration=75)
def generate(input_image, prompt="", guidance_scale=3.5, num_inference_steps=28, num_images=2, seed=None, aspect_ratio="1:1", progress=gr.Progress(track_tqdm=True)):
    try:
        logger.info(f"Starting generation with prompt: {prompt}")
        
        if input_image is None:
            raise ValueError("No input image provided")
            
        if seed is not None:
            torch.manual_seed(seed)
            logger.info(f"Set random seed to: {seed}")
             
        # Process image with Qwen2VL
        logger.info("Processing input image with Qwen2VL...")
        qwen2_hidden_state, image_grid_thw = process_image(input_image)
        logger.info("Image processing completed")
        
        # Compute text embeddings
        logger.info("Computing text embeddings...")
        pooled_prompt_embeds = compute_text_embeddings(prompt)
        t5_prompt_embeds = compute_t5_text_embeddings(prompt)
        logger.info("Text embeddings computed")
        
        # Move Transformer and VAE to GPU
        logger.info("Moving Transformer and VAE to GPU...")
        transformer.to(DEVICE)
        vae.to(DEVICE)
        
        # Update pipeline models
        pipeline.transformer = transformer
        pipeline.vae = vae
        logger.info("Models moved to GPU")
        
        # Get dimensions
        width, height = ASPECT_RATIOS[aspect_ratio]
        logger.info(f"Using dimensions: {width}x{height}")
        
        try:
            logger.info("Starting image generation...")
            output_images = pipeline(
                prompt_embeds=qwen2_hidden_state.to(DEVICE).repeat(num_images, 1, 1),
                pooled_prompt_embeds=pooled_prompt_embeds,
                t5_prompt_embeds=t5_prompt_embeds.repeat(num_images, 1, 1) if t5_prompt_embeds is not None else None,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                height=height,
                width=width,
            ).images
            logger.info("Image generation completed")
            
            return output_images
            
        except Exception as e:
            raise RuntimeError(f"Error generating images: {str(e)}")
            
    except Exception as e:
        logger.error(f"Error during generation: {str(e)}")
        raise gr.Error(f"Generation failed: {str(e)}")

# Create Gradio interface
with gr.Blocks(
    theme=gr.themes.Soft(),
    css="""
        .container { 
            max-width: 1200px; 
            margin: auto;
        }
        .header { 
            text-align: center; 
            margin: 20px 0 40px 0;
            padding: 20px;
            background: #f7f7f7;
            border-radius: 12px;
        }
        .param-row {
            padding: 10px 0;
        }
        footer {
            margin-top: 40px;
            padding: 20px;
            border-top: 1px solid #eee;
        }
    """
) as demo:
    with gr.Column(elem_classes="container"):
        gr.Markdown(
            """# 🎨 Qwen2vl-Flux Image Variation Demo
Generate creative variations of your images with optional text guidance"""
        )
        
        with gr.Row(equal_height=True):
            with gr.Column(scale=1):
                input_image = gr.Image(
                    label="Upload Your Image",
                    type="pil",
                    height=384,
                    sources=["upload", "clipboard"]
                )
                prompt = gr.Textbox(
                    label="Text Prompt (Optional)",
                    placeholder="As Long As Possible...",
                    lines=3
                )
                with gr.Accordion("Advanced Settings", open=False):
                    with gr.Group():
                        
                        with gr.Row(elem_classes="param-row"):
                            guidance = gr.Slider(
                                minimum=1,
                                maximum=10,
                                value=3.5,
                                step=0.5,
                                label="Guidance Scale",
                                info="Higher values follow prompt more closely"
                            )
                            steps = gr.Slider(
                                minimum=1,
                                maximum=50,
                                value=28,
                                step=1,
                                label="Sampling Steps",
                                info="More steps = better quality but slower"
                            )
                            
                        with gr.Row(elem_classes="param-row"):
                            num_images = gr.Slider(
                                minimum=1,
                                maximum=4,
                                value=1,
                                step=1,
                                label="Number of Images",
                                info="Generate multiple variations at once"
                            )
                            seed = gr.Number(
                                label="Random Seed",
                                value=None,
                                precision=0,
                                info="Set for reproducible results"
                            )
                            aspect_ratio = gr.Radio(
                                label="Aspect Ratio",
                                choices=["1:1", "16:9", "9:16", "2.4:1", "3:4", "4:3"],
                                value="1:1",
                                info="Choose aspect ratio for generated images"
                            )
                
                submit_btn = gr.Button(
                    "🎨 Generate Variations",
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=1):
                # Output Section
                output_gallery = gr.Gallery(
                    label="Generated Variations",
                    columns=2,
                    rows=2,
                    height=700,
                    object_fit="contain",
                    show_label=True,
                    allow_preview=True,
                    preview=True
                )
                error_message = gr.Textbox(visible=False)
        
        with gr.Row(elem_classes="footer"):
            gr.Markdown("""
                ### Tips:
                - 📸 Upload any image to get started
                - 💡 Add an optional text prompt to guide the generation
                - 🎯 Adjust guidance scale to control prompt influence
                - ⚙️ Increase steps for higher quality
                - 🎲 Use seeds for reproducible results
            """)
    
    submit_btn.click(
        fn=generate,
        inputs=[
            input_image,
            prompt,
            guidance,
            steps,
            num_images,
            seed,
            aspect_ratio
        ], 
        outputs=[output_gallery],
        show_progress=True
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",  # Listen on all network interfaces
        server_port=7860,       # Use a specific port
        share=False,            # Disable public URL sharing
        ssr_mode=False          # Fixes bug for some users
    )