'''
page_获取element里的代码 不是网页源代码
网易云是动态加载 我们不能在网页源代码中找到歌曲的名字
我们能在控制台的代码中找到歌曲的名字 说明当前获取到的是element中的代码
'''
from selenium import webdriver

import time
drive = webdriver.Chrome()
drive.get('https://music.163.com/#/discover/toplist')
time.sleep(2)
# 进入iframe
drive.switch_to.frame('g_iframe')

# 获取element里的代码 不是网页源代码
data = drive.page_source
print(data)
