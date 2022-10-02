'''
线程间的数据是共享的
如果数据过大会发生混乱
互斥锁 --> 解决资源混乱问题
lock() 不能重复上锁
rlock() 可以重复上锁
只上锁不解锁会造成死锁的情况 上几把 解几把
'''
import threading
import time
lock = threading.Lock()  # 创建一把锁
num = 0
def demo01():
    # 子线程1 对数据做写操作
    global num
    lock.acquire()  # 上锁
    for i in range(1000000):
        # 如果在函数里需要用到函数外的变量并且需要更变他 加global
        num += 1
    print('demo01', num)
    # lock.release()  # 解锁



def demo02():
    # 子线程2 对数据进行读取
    global num
    lock.acquire()  # 上锁
    for i in range(1000000):
        # 如果在函数里需要用到函数外的变量并且需要改变他 加global 申明当前我们使用的是个全局变量
        num += 1
    print('demo02', num)
    lock.release()  # 解锁


if __name__ == '__main__':
    t1 = threading.Thread(target=demo01)
    t2 = threading.Thread(target=demo02)
    t1.start()
    # time.sleep(2)  # 强制休息两秒 可能线程1只需要1秒的时间 浪费
    t2.start()
    # t2.join()



    print('main', num)