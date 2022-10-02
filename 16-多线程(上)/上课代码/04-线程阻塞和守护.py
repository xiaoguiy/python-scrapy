import time
import threading  # 内置模块threading传入一个函数对象
def sing():  # 第一个子线程
    for i in range(3):
        print(f'岁岁正在唱歌{i}')
        time.sleep(1)  # 看效果 假设程序遇到阻塞

def dance():  # 第二个子线程
    for i in range(3):
        print(f'岁岁在在跳舞{i}')
        time.sleep(1)

if __name__ == '__main__':  # 程序主入口 主线程
    # 两个子线程 一个主线程
    # 创建第1个子线程
    t1 = threading.Thread(target=sing)  # 传入函数对象 target=函数对象
    # 创建第2个子线程
    t2 = threading.Thread(target=dance)
    # 启动开启线程(当前线程准备就绪 等待cpu调度 具体时间是由cpu决定的)
    t1.start()  # 其实就是执行sing函数
    t2.start()
    t1.join()  # 让主线程等待sing函数执行完(线程都开启之后 再等待)
    t2.join()  # 让主线程等待dance函数执行完
    # 主线程不会等待子线程结束再往下执行
    # 如果想要主线程等待子线程 join()
    print('我是主线程')
