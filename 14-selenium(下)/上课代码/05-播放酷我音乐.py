from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
drive = webdriver.Chrome()
# 1.打开酷我音乐界面
drive.get('http://yinyue.kuwo.cn/')
time.sleep(2)
drive.maximize_window()
time.sleep(1)
# 2.定位到搜索框 搜索歌曲名字
drive.find_element_by_class_name('search').send_keys('水星记')

# 3.回车 给点时间等待 让页面加载完整
drive.find_element_by_class_name('search').send_keys(Keys.ENTER)
time.sleep(2)

# 4.实例化对象
actions = ActionChains(drive)
# 5.找到歌曲的位置
element_music = drive.find_element_by_xpath('//ul[@class="search_list"]/li')
print(element_music)
# 6.将鼠标移动到element上面
actions.move_to_element(element_music)
time.sleep(1)

# 提交事件(关门)
actions.perform()
# 4.定位播放按钮 点击操作
# 问题1:报错?
# 播放按钮是一个影藏标签 只有我们把鼠标滑到上面元素才会显示 所以我们应该先把鼠标滑到上面再做点击
# 法1：普通点击
# drive.find_element_by_xpath('//div[@class="song_opts flex_c"]/i[1]').click()
# 问题2:假设点击按钮失效
# 解决:js代码点击
el = drive.find_element_by_xpath('//div[@class="song_opts flex_c"]/i[1]')
# 法2:js点击
drive.execute_script("arguments[0].click()", el)

