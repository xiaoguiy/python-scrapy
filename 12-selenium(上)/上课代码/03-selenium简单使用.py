# 1.导入
from selenium import webdriver
# 2.加载驱动(调用本地的谷歌浏览器)
drive = webdriver.Chrome()
# 3.加载网页(请求页面 打开一个页面)
drive.get('https://www.baidu.com')

