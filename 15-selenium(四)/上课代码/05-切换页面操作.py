import time
from selenium import webdriver
drive = webdriver.Chrome()
# 打开第一个窗口
drive.get('https://www.baidu.com')
time.sleep(2)
# 打开第二个窗口
# drive.get('https://www.baidu.com')
drive.execute_script('window.open("https://www.douban.com/")')
# 打开两个窗口之后 鼠标定位在哪里?
# 鼠标定位在第二个窗口 能在第一个窗口定位嘛？
# drive.find_element_by_id('kw').send_keys('你好')
# 发生我们的鼠标是定位在第一个窗口--> 打开一个窗口肯定是想着操作它

# 窗口切换(从0开始)
drive.switch_to.window(drive.window_handles[1])  # 切换到豆瓣
print(drive.current_url)  # 当前页面的url
time.sleep(1)
drive.find_element_by_id('kw').send_keys('你好')  # 切换到豆瓣之后还能对百度进行操作嘛？不能
print(drive.current_url)

