from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
drive = webdriver.Chrome()
# 1.打开网易云页面
drive.get('https://music.163.com/')
time.sleep(1)
# 2.先定位到搜索框 输入一首歌
drive.find_element_by_id('srch').send_keys('水星记')
# 3.回车 给时间让页面加载完整
drive.find_element_by_id('srch').send_keys(Keys.ENTER)
time.sleep(5)

# 报错？我们的iframe标签是一个页面中嵌套了另一个页面
# 我们的webdriver只能在一个页面识别 我们的元素是在里面的那个页面
# 所以我们要先切入到里面的页面
# 4.解决:切入到iframe框架里面
# 通过id属性值g_iframe找到iframe标签 再切入
drive.switch_to.frame('g_iframe')

# 5.定位到播放按钮 点击
# drive.find_element_by_id('song_441491828').click()
drive.find_element_by_xpath('//div[@class="hd"]/a').click()