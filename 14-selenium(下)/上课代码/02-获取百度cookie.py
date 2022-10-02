from selenium import webdriver
import time
drive = webdriver.Chrome()
drive.get('https://www.baidu.com/')
time.sleep(2)
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


