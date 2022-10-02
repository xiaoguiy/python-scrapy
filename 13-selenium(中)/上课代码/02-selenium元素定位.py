from selenium import webdriver
drive = webdriver.Chrome()
# 加载百度页面
drive.get('https://www.baidu.com')
# 定位到输入框 搜索一个内容 往输入框填充内容
# send_keys(搜索内容)
# 1.通过id对标签进行定位
# drive.find_element_by_id('kw').send_keys('python')

# 为什么代码上有横线 运行不报错?
# 原因:selenium版本高 语法比较老 不支持
# 解决1：降低版本 或者说重新指定安装3.14.1
# 解决2：导入大By 语法有点不一样
from selenium.webdriver.common.by import By
# drive.find_element(By.ID, 'kw').send_keys('python')

# 2.通过class对标签进行定位
# drive.find_element_by_class_name('s_ipt').send_keys('python')
# drive.find_element(By.CLASS_NAME, 's_ipt')

# 3.通过name对标签进行定位
# drive.find_element_by_name('wd').send_keys('python')
# drive.find_element(By.NAME, 'wd')

# 4.通过xpath对标签进行定位(如果通过别的定位不到 就用xpath)
# drive.find_element_by_xpath('//input[@id="kw"]').send_keys('python')

# 5.通过标签名对标签进行定位 find_element() 返回第一个满足条件的标签
# input_tag = drive.find_element_by_tag_name('input').send_keys('你好')

# 一个页面不可能只有一个input标签 如果想找到多个 加s (elements)
# input_tag = drive.find_elements_by_tag_name('input')
# print(len(input_tag))  # 返回结果是列表

# 6.通过css选择器对标签进行定位 id=kw --> #kw
drive.find_element_by_css_selector('#kw').send_keys('你好')




