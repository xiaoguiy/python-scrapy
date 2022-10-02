# 1.导入
from selenium import webdriver
import time
# time模块做什么用? 程序快？ 页面加载快？页面没有加载出来获取不到数据 所以可以让程序延迟几秒
# 2.加载驱动(调用本地的谷歌浏览器)
drive = webdriver.Chrome(executable_path=r'D:\python\chromedriver.exe')
# 3.加载网页(请求页面 打开一个页面)
drive.get('https://www.baidu.com')
# 窗口最大化
drive.maximize_window()
time.sleep(3)  # 强制等待3秒
# 关闭当前窗口
# drive.close()
# 关闭所有窗口(关闭浏览器)
drive.quit()

