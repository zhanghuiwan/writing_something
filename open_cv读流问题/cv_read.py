import cv2
import time

cap = cv2.VideoCapture(0)
cnt = 0
pre_time = time.time() - 3
while True: 
    success,img = cap.read()
    assert success ,"video read finish"
    
    # if time.time() - pre_time < 3:
    #     continue
    # cv2.imshow(window_name,img)
    time.sleep(3)
    cnt += 1
    pre_time = time.time()
    cv2.imwrite(f"./pic_{cnt}.jpg", img)
    print(f"save {cnt}")
    if cnt > 5:
        break
# # 这段代码保存图片每张间隔6秒，cnt = 0
# pre_time = time.time() - 3
# while True: 
#     success,img = cap.read()
#     assert success ,"video read finish"
    
#     # if time.time() - pre_time < 3:
#     #     continue
#     # cv2.imshow(window_name,img)
#     time.sleep(3)
#     cnt += 1
#     pre_time = time.time()
#     cv2.imwrite(f"./pic_{cnt}.jpg", img)
#     print(f"save {cnt}")
#     if cnt > 5:
# #break这段代码则报错的6张图片都是相同的，仔细阅读代码，根据cap.read()，分析原因
    
import cv2
import threading

class VideoStreamThread:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        self.frame = None
        self.running = True
        self.lock = threading.Lock()

        # 启动线程
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while self.running:
            success, frame = self.cap.read()
            if success:
                # 使用锁更新帧，确保线程安全
                with self.lock:
                    self.frame = frame

    def read(self):
        # 使用锁读取最新帧
        with self.lock:
            return self.frame

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()

# 使用线程读取视频流
video_stream = VideoStreamThread(0)

while True:
    frame = video_stream.read()
    if frame is not None:
        cv2.imshow("Latest Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_stream.stop()
cv2.destroyAllWindows()