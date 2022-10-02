import time
from selenium import webdriver
drive = webdriver.Chrome()
drive.get('https://movie.douban.com/top250?start=0&filter=')
time.sleep(2)
# 1.通过链接文本内容定位按钮
# page = drive.find_element_by_link_text('后页>')
# print(page)
# page.click()

# 2.标签对象.get_attribute(属性名)
# 获取img标签中的src属性值
# img_tag = drive.find_element_by_xpath('//div[@class="pic"]/a/img')
# print(img_tag)
# print(img_tag.get_attribute('src'))

# 3.text 获取子节点和孙节点的文本内容
# 找到a标签 获取a标签下面span标签的文本内容
a_tag = drive.find_element_by_xpath('//div[@class="hd"]/a/span')
print(a_tag)
print(a_tag.text)
