[Gradio官方教程一：Gradio生态系统、主要组件及Interface class简介](https://blog.csdn.net/qq_56591814/article/details/139886612)

[Gradio入门详细教程](https://blog.csdn.net/weixin_45277161/article/details/134998849)

```python
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
```