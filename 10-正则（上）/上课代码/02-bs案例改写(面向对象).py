import requests
from bs4 import BeautifulSoup
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
class Weather():
    lst = []  # 类属性
    def __init__(self):
        list_url = [
            'http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml',
            'http://www.weather.com.cn/textFC/gat.shtml',
        ]
        for url in list_url:
            # html表示每一个地区的网页源代码
            html = self.get_data(url)
            lst = self.parse_data(html)
            self.sava_data()
    # 发生请求
    def get_data(self, url):
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        data = response.text
        return data
    # 解析数据
    def parse_data(self, data):
        soup = BeautifulSoup(data, 'html5lib')
        # 先找到class属性为conMidtab的div标签 当前div中包含了五个省份的信息
        conMidtab = soup.find('div', class_="conMidtab")
        # 在总的(conMidtab)下面找所有table标签
        tables = conMidtab.find_all('table')  # 返回值 列表
        for tab in tables:
            # tab表示每一个省 在省份下面找tr(一个tr标签就是一个城市的信息)
            tr_tag = tab.find_all('tr')[2:]  # 前面两个tr不要
            # 在每一个城市下面找td(城市名字td[0] 最低温度td[-2])
            for index, tr in enumerate(tr_tag):
                dic = {}
                # 如果index的值==0 就说明当前这个是第一个tr标签(省会城市) 取td[1]
                # 如果不为0  就是普通城市 取td[0]
                one_td = tr.find_all('td')[0]
                if index == 0:
                    one_td = tr.find_all('td')[1]
                # tr表示一个城市的信息
                # stripped_strings 获取当前节点下面的子节点的文本内容
                city_name = list(one_td.stripped_strings)[0]
                two_td = tr.find_all('td')[-2]
                temp = list(two_td.stripped_strings)[0]
                dic['city'] = city_name
                dic['temp'] = temp
                self.lst.append(dic)
    # 保存数据
    def sava_data(self):
        with open('tianqi1.csv', 'w', encoding='utf-8', newline='') as f:
            write = csv.DictWriter(f, fieldnames=['city', 'temp'])
            write.writeheader()
            write.writerows(self.lst)

w = Weather()


