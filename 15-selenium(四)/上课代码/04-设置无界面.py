'''
不用再打开浏览器 也能操作界面
节省时间
'''
import time
from selenium import webdriver

# 1.创建对象
options = webdriver.ChromeOptions()
# 2.设置无界面模式
options.add_argument('--headless')
# 3.加载驱动 传入参数
drive = webdriver.Chrome(options=options)

drive.get('https://movie.douban.com/top250?start=0&filter=')
time.sleep(2)
a_tag = drive.find_element_by_xpath('//div[@class="hd"]/a')
print(a_tag)
print(a_tag.text)
