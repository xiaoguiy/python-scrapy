from selenium import webdriver
import time
drive = webdriver.Chrome()
drive.get('https://qzone.qq.com/')
# 1.进入iframe
drive.switch_to.frame('login_frame')

# 2.找到岁岁的头像 进行点击(点击之后就会进入到登录的状态)
drive.find_element_by_id('img_out_2825262812').click()
# 让页面加载完整
time.sleep(3)

# 3.获取qq空间的cookie
cookie = drive.get_cookies()
# 我们用get_cookies()获取的cookie信息和平常不一样 [{}，{}，{}]
li = []
for dic in cookie:
    # dic当前是字典
    # print(dic)
    # 通过键获取值
    name = dic.get('name')
    value = dic['value']
    # print(name, value)
    # break
    # 键=值
    li.append(name+'='+value)

# 我们在网页中看到的cookie格式
cookie_detail = '; '.join(li)
print(cookie_detail)


