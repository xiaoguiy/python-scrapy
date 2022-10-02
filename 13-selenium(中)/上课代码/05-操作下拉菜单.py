'''
17素材-搜索select-select下拉菜单-最后面两个
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
drive = webdriver.Chrome()
# drive.get('https://www.17sucai.com/pins/demo-show?id=7417&st=eYd1x2OjX10C28GPghywbg&e=1660837172')
# 普通对象下拉框操作
# 0.先进入iframe标签里面
# drive.switch_to.frame('iframe')
# 1.定位到p标签 点击
# drive.find_element_by_class_name('set').click()
# time.sleep(2)
# 2.选择下拉菜单的选项 点击不同的li标签(xpath下标从1开始)
# ul_tag = drive.find_element_by_xpath('//ul[@class="new"]/li[3]')
# ul_tag.click()
# print(ul_tag)

# select对象(下拉菜单是select标签组成)
drive.get('https://www.17sucai.com/pins/demo-show?id=7362&st=7RLCtYobl4UioQlXEIISLA&e=1660837968')
from selenium.webdriver.support.ui import Select

# 进入iframe标签中
drive.switch_to.frame('iframe')
# 实例化select对象  Select(select标签对象)
select_tag = Select(drive.find_element_by_name('D1'))
# 根据索引去进行定位(从0开始)
time.sleep(3)
# select_tag.select_by_index(1)
# 根据属性值去进行定位
select_tag.select_by_value('3')


