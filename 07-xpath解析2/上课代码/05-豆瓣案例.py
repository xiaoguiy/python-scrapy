import requests
from lxml import etree
import csv
url = 'https://movie.douban.com/top250'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
# data是网页源代码
data = response.text
html = etree.HTML(data)
# 每一个div标签里就包含了一个电影的信息
div_tag = html.xpath('//div[@class="info"]')
# print(len(div_tag))  # 25
for div in div_tag:
    # div就表示每一个电影的信息
    # 电影名字
    title = div.xpath('./div[@class="hd"]/a/span[1]/text()')  # 列表
    # 评分
    '''
    //div[@class="info"] --> .
    '''
    pingfen = div.xpath('./div[@class="bd"]/div/span[2]/text()')
    # 引言
    yinyan = div.xpath('./div[@class="bd"]/p/span/text()')
    # print(yinyan)
    # 详情页url
    x_url = div.xpath('./div[@class="hd"]/a/@href')
    print(x_url)



