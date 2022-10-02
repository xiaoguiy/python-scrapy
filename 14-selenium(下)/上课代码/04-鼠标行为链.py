from selenium import webdriver
from selenium.webdriver import ActionChains
import time
drive = webdriver.Chrome()
drive.get('https://www.baidu.com')
time.sleep(1)
# 找到输入框
input_tag = drive.find_element_by_id('kw')
# 找到百度一下按钮
button_tag = drive.find_element_by_id('su')

# 实例化对象
actions = ActionChains(drive)
# 输入内容搜索
actions.send_keys_to_element(input_tag, 'python')
# 注意2：
# 实例化对象和提交事件中间存放的内容必须是跟行为链有关(通过actions去调用)
# 实例化对象和提交事件之间形成了一个队列
# 注意1:提交事件!
actions.perform()

button_tag.click()  # 不属于行为链的内容 放到提交事件之后



