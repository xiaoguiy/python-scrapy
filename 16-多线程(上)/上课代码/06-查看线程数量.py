'''
1.首先线程必须是存活的状态(函数还没有运行完)
2.如果线程结束了就说明线程不是存活的状态
'''
import time
import threading  # 内置模块threading传入一个函数对象
def sing():  # 第一个子线程
    for i in range(3):
        print(f'岁岁正在唱歌{i}')
        time.sleep(1)  # 看效果 假设程序遇到阻塞

def dance():  # 第二个子线程
    for i in range(6):
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
    # print('我是主线程')
    while True:  # 让主线程一直不退出
        print(threading.enumerate())  # 查看线程数量 返回的是列表
        # 只剩主线程就结束
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)
