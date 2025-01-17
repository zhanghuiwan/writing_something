import gradio as gr
from ultralytics import YOLO


model = YOLO('yolov8n.pt')  

def predict(image, iou = 0.5, conf = 0.5):
    results = model(image, iou = iou, conf = conf)
    
    if results:
        result = results[0]
        annotated_frame = result.plot()
        return annotated_frame
    else:
        return image  

# 创建Gradio接口
demo = gr.Interface(
    fn=predict, 
    inputs=[gr.Image(), gr.Slider(0, 1, 0.5, 0.1), gr.Slider(0, 1, 0.5, 0.1)], 
    outputs=gr.Image(),
)

# 启动Gradio应用
if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', server_port=8080, show_error=True)