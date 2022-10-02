from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

class JdBook(object):
    lst = []  # 类属性  在整个类里面是通用的
    # 1.初始化方法(加载驱动)
    def __init__(self):

        self.drive = webdriver.Chrome()
        self.drive.get('https://www.jd.com/?')
        time.sleep(2)
        # 定位输入框输入内容
        self.drive.find_element_by_id('key').send_keys('爬虫书')
        # 输入回车
        self.drive.find_element_by_id('key').send_keys(Keys.ENTER)
        time.sleep(1)
    # 数据随着鼠标的拖动才加载完整的  想办法把滚动条滚到最下面
    # 2.解析数据
    def parse_data(self):
        # window.scrollTo(最上面,整个窗口的高度(最底部))
        self.drive.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(2)
        # 找到所有li标签 一个li表示一本书的信息(elements 列表)
        book_list = self.drive.find_elements_by_xpath('//div[@id="J_goodsList"]/ul/li')
        for book in book_list:
            # 加异常捕获 以防有的数据是空值影响后续数据的获取
            try:
                dic = {}
                # book是一个标签对象 表示每一个li标签
                # 价格
                # div[@class="p-price"]是属于li标签下 但是不是直属于 .代表当前节点 //不用在意是不是根节点
                # .//在当前节点不看位置
                dic['price'] = book.find_element_by_xpath('.//div[@class="p-price"]/strong').text
                # 书籍名字
                dic['book_name'] = book.find_element_by_xpath('.//div[@class="p-name"]/a').text
                # 评论条数
                dic['words'] = book.find_element_by_xpath('.//div[@class="p-commit"]/strong').text
                # 店铺名字
                dic['shop_name'] = book.find_element_by_xpath('.//div[@class="p-shopnum"]/a').text
                print(dic)
                self.lst.append(dic)
            except Exception as e:
                print(e)

    # 3.保存数据
    def save_data(self):
        with open('jd.csv','w',encoding='utf-8',newline='') as f:
            pass

    # 4.主函数
    def mian_jd(self):
        while True:
            # 没有到最后一页就继续翻 怎么判断有没有到最后一页？
            # 如果没有到最后一页 就继续翻页
            # 如果在当页页面没有找到pn-next disabled 就返回-1 说明还没有到最后一页 --> 接着解析翻页
            if self.drive.page_source.find('pn-next disabled') == -1:
                self.parse_data()
                # 解析完当页的数据就翻页--> 点击下一页
                # 找到下一页的按钮
                self.drive.find_element_by_class_name('pn-next').click()
                time.sleep(3)
            # 如果到最后一页 结果循环 退出页面
            else:
                # 值等于-1 --> 到了最后一页 --> 退出
                break
        # while循环结束意味着100页数据已经获取完成
        self.save_data()


j = JdBook()
j.mian_jd()