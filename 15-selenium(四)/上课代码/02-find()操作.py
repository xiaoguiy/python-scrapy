'''
如果我想获取1-最后一页 在不知道页数的情况下怎么办 ？怎么知道这个网站有多少页？
一般倒数第二页和倒数第二页的翻页按钮有点差别 

'''
import time
from selenium import webdriver
drive = webdriver.Chrome()
drive.get('https://www.baidu.com')
time.sleep(2)
data = drive.page_source  # 字符串
print(data.find('kw'))  # 5598 下标 当前字符存在于字符串中的一个位置
print(data.find('期'))  # -1
