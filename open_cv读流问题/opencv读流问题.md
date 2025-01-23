

## OpenCV读流问题

### 结论
这里直接给结论吧

具体的底层原理也不太清楚，过慢读流会导致帧堆积，获取到的不是实时图片。

- 使用线程或者进程读流
- 考虑读流失败重新连接的问题

```python
class VideoStreamThread:
    def __init__(self, source):
        self.source = source
        self.cap = cv2.VideoCapture(self.source)
        self.frame = None
        self.running = True
        self.lock = threading.Lock()

        # 启动线程
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while self.running:
            success, frame = self.cap.read()
            if not success:
                self.cap.release()
                self.cap = cv2.VideoCapture(self.source)
            if success:
                # 使用锁更新帧，确保线程安全
                with self.lock:
                    self.frame = frame

    def read(self):
        # 使用锁读取最新帧
        with self.lock:
            if self.frame is not None:
                return True, self.frame
            else:
                return False, None

    def stop_read(self):
        self.running = False
        self.thread.join()
        self.cap.release()
    
    def get(self, arge):
        return self.cap.get(arge)
    
cap = VideoStreamThread(rtspUrl)
while True:
    success, frame = cap.read()
    if not success:
        print(f"读取帧失败")
        break
   	other_task()
cap.release()
```


### 测试代码

#### 1.正常读流

- 根据保存的图片看，每一帧保存一次图片

```python
import cv2
import time

source = "rtsp://admin:byd@2024@10.12.3.237:554/h264/ch1/main/av_stream"
cap = cv2.VideoCapture(source)

cnt = 1
start_time = time.time()
while True:
    success, frame = cap.read()
    if not success:
        print(f"读取第{cnt}帧失败")
        break
    cv2.imwrite(f"./pic/pic_{cnt}.jpg", frame)
    print(f"save {cnt}")
    cnt += 1

    if cnt > 2:
        print(f"读取完{cnt}帧")
        break

duration = time.time() - start_time
print(f"读完{cnt}帧，花费时间 {duration} 秒")

cap.release()

```

#### 2. 测试read时间

如果读取速度过快，导致read时opencv的缓存队列中没有帧，read函数会等待队列中有帧之后读取

![1737167337630](opencv读流问题.assets/1737167337630.png)


```python
import cv2
import time

source = "rtsp://admin:byd@2024@10.12.3.237:554/h264/ch1/main/av_stream"
cap = cv2.VideoCapture(source)

cnt = 1
start_time = time.time()
start_read_time_list = []
end_read_time_list = []
end_loop_time_list = []
while True:
    if cnt > 1000:
        print(f"读取完{cnt}帧")
        break
    start_read_time = time.time()
    start_read_time_list.append(start_read_time)
    success, frame = cap.read()
    end_read_time = time.time()
    end_read_time_list.append(end_read_time)
    # print(f"read 的时间为{end_read_time - start_read_time} 秒")
    if not success:
        print(f"读取第{cnt}帧失败")
        break
    # cv2.imwrite(f"./pic/pic_{cnt}.jpg", frame)
    # print(f"save {cnt}")
    cnt += 1

    
    end_loop_time = time.time()
    end_loop_time_list.append(end_loop_time)
    # print(f"写图片时间为{end_loop_time - end_read_time} 秒， 循环总时间为{end_loop_time - start_read_time} 秒")
duration = time.time() - start_time
print(f"读完{cnt - 1}帧，花费时间 {duration} 秒")

print(f"read时间{sum(end_read_time_list) - sum(start_read_time_list)}, 处理时间{sum(end_loop_time_list) - sum(end_read_time_list)} , loop time {sum(end_loop_time_list) - sum(start_read_time_list)}")

cap.release()

```

#### 3. 加大处理时间

- sleep2秒，sleep10秒都固定读取到30帧时失败，且全都是按顺序读取的帧（1秒的25帧+下一秒的4帧）

-  帧缓存队列会堆积，每次读取都是读取缓存队列中的帧。该方法会导致opencv的缓存队列满而发生读取流失败

WHY？？？

> Could you check playback with ffmpeg and/or vlc? Do they work well with the stream for more than 10-15 minutes? The error means that the stream is corrupted. H264 is stateful and cannot start decoding from random place. The errors you mentioned may appear if:
>
> - Camera produces corrupted stream
> - The network connection is poor: data loss, not enough speed.
> - Consumer does not consume all frames in time. FFmpeg back-end have to drop packages, if buffer is full and it breaks playback.

https://github.com/opencv/opencv/issues/25889