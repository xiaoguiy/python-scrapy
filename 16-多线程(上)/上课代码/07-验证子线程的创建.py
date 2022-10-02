import time
import threading  # 内置模块threading传入一个函数对象
def sing():  # 第一个子线程
    for i in range(3):
        print(f'岁岁正在唱歌{i}')
        time.sleep(1)  # 看效果 假设程序遇到阻塞

if __name__ == '__main__':  # 程序主入口 主线程
    # 创建第1个子线程
    print(threading.enumerate(), '创建之前')
    t1 = threading.Thread(target=sing)  # 传入函数对象 target=函数对象
    print(threading.enumerate(), '创建之后')
    # 启动开启线程(当前线程准备就绪 等待cpu调度 具体时间是由cpu决定的)
    t1.start()  # 开启子线程才是真正的创建一个线程
    print(threading.enumerate(), '启动之后')
