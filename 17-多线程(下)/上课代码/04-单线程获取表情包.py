'''
目标网站:https://www.fabiaoqing.com/biaoqing/lists/page/1.html
需求:获取1-10页的表情包 保存到本地

https://www.fabiaoqing.com/biaoqing/lists/page/2.html
https://www.fabiaoqing.com/biaoqing/lists/page/3.html
https://www.fabiaoqing.com/biaoqing/lists/page/4.html
'''
import requests
import re
from lxml import etree
import urllib.request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
count = 1
for i in range(1, 11):
    url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{i}.html'
    resposne = requests.get(url, headers=headers)
    data = resposne.text
    # 创建对象
    html = etree.HTML(data)
    img_tag = html.xpath('//img[@class="ui image lazy"]')  # 定位到所有img标签
    # print(len(img_tag))
    for img in img_tag:
        # 当前就是在img标签下 获取data-original属性值
        src = img.xpath('@data-original')[0]
        # 获取title属性值用来图片命名
        name = img.xpath('@title')[0]
        # urlretrieve(图片链接,图片名字)
        # name = name.replace('?', '')
        # 保存图片时 有些符号不允许作为文件命名 替换为空 replace可以 但是麻烦
        name = re.sub('[\/:*?"<>|]','', name)
        urllib.request.urlretrieve(src, f'img/{name}{count}.jpg')
        print(f'第{count}张下载完毕!')
        count += 1
        # print(src, name)


