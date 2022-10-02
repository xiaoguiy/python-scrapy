import threading
import time

def task(a):  # 11传递给a
    print(a)  # 11
    time.sleep(5)
    print('任务')

t = threading.Thread(target=task, args=(11,))  # args=元组
t.setDaemon(True)  # 主线程结束 子线程必须也要结束
t.start()
print('END')  # 主线程

