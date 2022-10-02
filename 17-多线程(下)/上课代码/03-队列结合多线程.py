import threading
import time
from queue import Queue
def put_data(q):
    # 往队列中放入数据
    num = 0
    while True:
        q.put(num)
        num += 1
        # time.sleep(1)

def get_data(q):
    # 往队列中获取数据
    while True:
        print(q.get())


if __name__ == '__main__':
    q = Queue(5)  # 创建队列 一边放一边拿 队列一直就是空的 如果队列是满的 会等着拿出来
    # 创建线程
    t1 = threading.Thread(target=put_data, args=(q, ))
    t2 = threading.Thread(target=get_data, args=(q, ))
    t1.start()
    t2.start()
