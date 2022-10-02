'''
https://www.sogou.com/web?query=%E4%BD%A0%E5%A5%BD
https://www.sogou.com/web?query=%E4%B8%AD%E5%9B%BD

https://www.sogou.com/web?query=%E4%B8%AD%E5%9B%BD&page=3
https://www.sogou.com/web?query=%E4%B8%AD%E5%9B%BD&page=4
'''

import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
# 中国 1 3
key = input('请输入你的搜索内容:')
start = int(input('请输入你的起始页:'))
end = int(input('请输入你的结束页:'))
for i in range(start, end+1):
    # i表示页数
    url = f'https://www.sogou.com/web?query={key}&page={i}'
    response = requests.get(url, headers=headers)
    with open(f"{key}第{i}页.html", 'w',encoding='utf-8') as f:
        f.write(response.text)
