import requests
from lxml import etree
import csv
# 拿到网页源代码
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
def get_data(url):
    response = requests.get(url, headers=headers)
    # data是网页源代码
    data = response.text
    return data  # 函数的返回值返回到函数调用的地方

# 解析数据
def parse_data(data):
    html = etree.HTML(data)
    # 每一个div标签里就包含了一个电影的信息
    div_tag = html.xpath('//div[@class="info"]')
    # print(len(div_tag))  # 25
    lst = []
    for div in div_tag:
        dic = {}
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
        # print(x_url)
        dic['title'] = title[0]
        dic['pingfen'] = pingfen[0]
        dic['yinyan'] = yinyan[0] if yinyan else None
        dic['x_url'] = x_url[0]
        print(dic)
        lst.append(dic)
    # for循环结束意味着我们当前页面的数据已经构建完成
    return lst

# 保存数据
def save_data(lst):
    with open('douban.csv', 'w', encoding='utf-8', newline='') as f:
        write = csv.DictWriter(f, fieldnames=['title', 'pingfen', 'yinyan', 'x_url'])
        # 写入表头
        write.writeheader()
        # 写入数据
        write.writerows(lst)

lst_all = []
for i in range(1, 11):
    url = f'https://movie.douban.com/top250?start={(i-1)*25}&filter='
    # html是每一页的网页源代码
    html = get_data(url)
    # lst是每一页解析好后的数据
    lst = parse_data(html)
    lst_all += lst
# 拿到存放十页的列表数据之后再保存
save_data(lst_all)


# 一页的数据保存一次 一页的数据返回结果是列表 可不可以等十页数据都拿到之后再一次性写入？


