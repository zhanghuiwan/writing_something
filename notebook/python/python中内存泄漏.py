import gc
import tracemalloc

# 开启垃圾回收器调试模式，打印所有收集到的对象信息
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_cycle():
    # 创建两个对象，形成循环引用
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node2.next = node1

def main():
    tracemalloc.start()  # 开始跟踪内存分配
    
    snapshot1 = tracemalloc.take_snapshot()
    
    for _ in range(1000):  # 创建大量的循环引用
        create_cycle()

    snapshot2 = tracemalloc.take_snapshot()
    
    # 对比两次快照之间的差异，找出新增加的内存分配
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    
    print("[ Top 10 differences ]")
    for stat in top_stats[:10]:
        print(stat)
    
    # 强制进行垃圾回收
    collected = gc.collect()
    print(f"Garbage collector: collected {collected} objects.")

if __name__ == "__main__":
    main()