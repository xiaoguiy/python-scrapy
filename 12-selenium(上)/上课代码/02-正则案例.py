import requests
import re
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = 'http://www.weather.com.cn/weather/101250101.shtml'
resposne = requests.get(url, headers=headers)
resposne.encoding = 'utf-8'
data = resposne.text  # 网页源代码(匹配内容)
# 1.匹配ul标签
ul_tag = re.match('.*(<ul class="t clearfix">.*?</ul>)', data, re.S)
ul = ul_tag.group(1)  # 提取匹配到的内容
# 2.匹配所有li标签
li_tag = re.findall('<li.*?>.*?</li>', ul, re.S)
lis = []
# 4.定义一个模板对象(匹配li标签)
pat = re.compile('<li.*?>.*?<h1>(.*?)</h1>.*?<p.*?>(.*?)</p>.*?<i>(.*?)</i>.*?<i>(.*?)</i>.*?</li>', re.S)
for li in li_tag:
    # li是每一天的信息(匹配内容)
    # 3.每一个li标签里的信息排版相同(匹配规则相同)
    res = pat.match(li)
    print(li)
    # 5.match对象.group()提取内容
    # print(res.group(1), res.group(2), res.group(3), res.group(4))
    tu = res.groups()  # 元组(第一天, 第二天, 第三天)
    # [[第一天],[第二天],[第三天]] --> Write [{},{},{}] --> DictWrite
    lis.append(tu)

print(lis)
with open('changsha.csv', 'w', encoding='utf-8',newline='') as f:
    # 写入对象
    write = csv.writer(f)
    # 写入表头
    write.writerow(['日期', '天气', '温度', '风力'])
    write.writerows(lis)
