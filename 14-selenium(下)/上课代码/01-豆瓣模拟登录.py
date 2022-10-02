from selenium import webdriver
import time
drive = webdriver.Chrome()
# 0.打开豆瓣页面
drive.get('https://www.douban.com/')
time.sleep(1)
# 1.切入iframe标签
#
iframe_tag = drive.find_element_by_xpath('//div[@class="login"]/iframe')
drive.switch_to.frame(iframe_tag)
# 2.点击'密码登录'切换界面
drive.find_element_by_class_name('account-tab-account').click()
time.sleep(1)
# 3.定位输入框 输入账号
drive.find_element_by_id('username').send_keys('xxx')
time.sleep(1)
# 4.定位输入框 输入密码
drive.find_element_by_id('password').send_keys('xxx')
time.sleep(1)
# 5.点击'登录豆瓣'按钮
# 注意：如果因为属性中有空格定位不到 --> 取空格的前的属性或者通过xpath定位
drive.find_element_by_class_name('btn').click()


