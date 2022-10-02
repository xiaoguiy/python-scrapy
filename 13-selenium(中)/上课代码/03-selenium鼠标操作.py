import time
from selenium import webdriver
drive = webdriver.Chrome()

# 加载百度页面
drive.get('https://www.baidu.com')
# 需求 1.定位到输入框
input_tag = drive.find_element_by_id('kw')
# 2.输入python
input_tag.send_keys('python')
time.sleep(1)
# 3.先定位到百度一下按钮 4.点击
# drive.find_element_by_id('su').click()
time.sleep(3)
# 4.清空输入框
input_tag.clear()


