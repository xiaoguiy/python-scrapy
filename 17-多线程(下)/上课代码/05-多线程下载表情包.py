import requests
from lxml import etree
import time
import re
import urllib.request
from queue import Queue
import threading
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
class Product(threading.Thread):  # 生产者
    # 在自定义类中写了init方法 调用父类Thread的init方法
    def __init__(self, page_url,img_url):
        super().__init__()
        # 初始化方法 将url拿到
        self.page_url = page_url
        self.img_url = img_url
        pass
    def run(self):
        # 让生产者拿到url去处理
        # 三个生产者 怎么去处理10个url？让生产者一直工作 直到队列为空(队列里的url处理完了)
        while True:
            # 如果队列为空 结束循环
            if self.page_url.empty():
                break
            else:
                # 如果队列不为空 拿到url去获取数据
                url = self.page_url.get()
                # 对url发生请求 进行解析 单独写一个解析数据的方法
            self.parse_data(url)

    # 解析数据
    def parse_data(self, url):
        resposne = requests.get(url, headers=headers)
        data = resposne.text
        time.sleep(1)
        # 创建对象
        html = etree.HTML(data)
        img_tag = html.xpath('//img[@class="ui image lazy"]')  # 定位到所有img标签
        print('检查', len(img_tag))  # 为0的情况 可能网页没有加载
        for img in img_tag:
            # 当前就是在img标签下 获取data-original属性值
            src = img.xpath('@data-original')[0]
            # 获取title属性值用来图片命名
            name = img.xpath('@title')[0]
            # urlretrieve(图片链接,图片名字)
            # name = name.replace('?', '')
            # 保存图片时 有些符号不允许作为文件命名 替换为空 replace可以 但是麻烦
            name = re.sub('[\/:*?"<>|]', '', name)
            # 拿到图片链接和图片名字-->放入新的队列-->再让消费者处理
            self.img_url.put((src, name))  # 以元组的方式放进去
        print(self.img_url.qsize())  # 查看当前队列大小 检查


class Customer(threading.Thread):  # 消费者
    count = 1
    def __init__(self,img_url):
        super().__init__()
        # 初始化方法 将url拿到
        self.img_url = img_url
    def run(self):
        # 让消费者一直去工作 直到img_url队列中没有数据 才结束
        while True:
            # 如果队列是空的 就说明已经处理完了
            if self.img_url.empty():
                break
            # 否则 就先从队列中把图片链接 和图片名字 取出来  再下载
            else:
                # 取出来的img_data是一个元组 拆包
                img_data = self.img_url.get()
            url, name = img_data
            urllib.request.urlretrieve(url, f'img1/{name}{self.count}.jpg')
            print(f'第{self.count}张下载完毕!')
            self.count += 1


if __name__ == '__main__':
    # 1.创建一个存放url的队列
    page_url = Queue()
    # 问题解决:等所有的数据生产好之后 再消费
    for i in range(1, 11):
        url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{i}.html'
        page_url.put(url)  # 将构建好的10个url放入队列 --> 让生产者处理
    # 3.创建一个存放图片链接 图片名字的队列
    img_url = Queue()
    # 2.创建几个生产者(线程)处理url(拿到数据)
    t_lst = []
    for i in range(3):
        t = Product(page_url, img_url)  # 创建对象
        t.start()  # 开启线程 相当于run方法
        t_lst.append(t)
    for i in t_lst:
        i.join()
    # 4.创建消费者 --> 从img_url这个队列中拿数据 --> 保存
    for i in range(3):
        t1 = Customer(img_url)
        t1.start()

# 没有数据? img_url是空的 也就是说我们的程序是先消费的 再生产
# 我们应该先等所有数据生产完之后 才能去消费


