'''
法2：
1.自定义类继承threading.Thread
2.重写run方法
3.将线程要完成的放在run方法中

'''
import time
import threading
class MyThreading(threading.Thread):
    def run(self):
        for i in range(4):
            print(f'thread{i}')
            time.sleep(1)
            self.a()
            self.b()
    def a(self):
        pass
    def b(self):
        pass


class MyThreading1(threading.Thread):
    def run(self):
        for i in range(4):
            print(f'thread111{i}')
            time.sleep(1)

if __name__ == '__main__':
    m1 = MyThreading()
    m2 = MyThreading1()
    # 普通调用 不行
    # m1.run()
    # m2.run()
    # 启动线程
    m1.start()  # 相当于进入run方法
    m2.start()