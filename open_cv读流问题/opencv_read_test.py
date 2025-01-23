import cv2
import time
from datetime import datetime

source = "rtsp://admin:byd@2024@10.12.3.237:554/h264/ch1/main/av_stream"
cap = cv2.VideoCapture(source)

cnt = 1
start_time = time.time()

while True:
    success, frame = cap.read()
    if not success:
        print(f"读取第{cnt}帧失败")
        break
    print(datetime.now())
    cv2.imwrite(f"./pic/pic_{cnt}.jpg", frame)
    print(f"save {cnt}")
    cnt += 1

    if cnt > 2:
        print(f"读取完{cnt}帧")
        break

duration = time.time() - start_time
print(f"读完{cnt}帧，花费时间 {duration} 秒")

cap.release()