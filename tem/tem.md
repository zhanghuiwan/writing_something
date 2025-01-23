"Simulate a fire with burning flames and thick smoke in the given image."
"Add a raging fire to the center of the image, with intense orange flames and dark smoke."

"Add a realistic fire to the left side of the building in the image, with dark smoke rising into the sky."


	--denoise_strength：在 img2img 模式中控制生成结果的多样性。建议从 0.4 到 0.8 测试：
	•	较低值（如 0.4）：输出更接近原始图像。
	•	较高值（如 0.8）：输出与原图差异更大。
	•	--steps：增加步数可以提升生成质量，但会增加计算时间。默认 28，可以尝试增加到 50。
	•	--guidance_scale：控制提示词的引导强度，默认值为 3.5。可以尝试从 5 到 10 以加强提示词效果。


    python main.py --mode img2img \
               --input_image input.jpg \
               --prompt "A building engulfed in flames with thick smoke" \
               --denoise_strength 0.7 \
               --output_dir outputs
