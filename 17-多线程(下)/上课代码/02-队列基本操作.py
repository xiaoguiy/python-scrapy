'''
获取数据 保存数据
队列  解耦操作
耦合性太强:获取数据 保存数据 关联性太强
把获取到的数据放入队列中 下载数据从队列中取拿
'''
from queue import Queue
# maxsize 最大值 可以存多少个数据 默认不给参数(无限大 跟内存相关)
q = Queue(4)  # 创建对象(队列)
q.put(725)  # 把数据放进去
q.put('20')
q.put([1])
q.put([1, 2])
# print(q.full())  # 判断当前队列是否满了 True
q.put(3)  # 在队列已经满了的情况下再继续放 不行 超出会发生阻塞
print('取出前', q.qsize())  # 查看当前队列大小 4
data = q.get()  # 从队列中取数据 取的是最先放进去的数据
# print(data)
print('取出后', q.qsize())

