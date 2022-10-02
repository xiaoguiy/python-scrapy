import requests
from bs4 import BeautifulSoup
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = 'http://www.weather.com.cn/textFC/gat.shtml'
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
data = response.text
# print(data)

# 因为港澳台网页源代码并不是完整的 所以我们选择一个容错性更好的解析器-->html5lib(pip install html5lib)
soup = BeautifulSoup(data, 'html5lib')
lst = []
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
        lst.append(dic)

with open('tianqi.csv', 'w', encoding='utf-8',newline='') as f:
    write = csv.DictWriter(f, fieldnames=['city', 'temp'])
    write.writeheader()
    write.writerows(lst)







