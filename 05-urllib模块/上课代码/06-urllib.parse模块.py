'''
requests模块可以自己处理url中包含了中文的问题
urllib 不行 我们需要手动编码
原神 --> %E5%8E%9F%E7%A5%9E
%+十六进制数 三个百分号就代表一个中国汉字
编码 我们能看懂的数据 --> 计算机能看懂的数据
解码 计算机能看懂的数据--> 我们能看懂的数据
'''
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0'}
# url = 'https://tieba.baidu.com/f?ie=utf-8&kw=原神'
# url1 = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%8E%9F%E7%A5%9E'
# res = requests.get(url, headers=headers)
# print(res.url)

import urllib.request
# urllib.request.urlopen(url)  # 报错 不支持中文

import urllib.parse
key = input('请输入你搜索内容')
# 对汉字进行编码操作
# 1.urlencode(字典)
dic = {'kw': key}
# value = urllib.parse.urlencode(dic)
# print(value)  # kw=%E4%B8%AD%E5%9B%BD
# url2 = f'https://tieba.baidu.com/f?ie=utf-8&{value}'
# print(url2)

# 2.quote(字符串)
value1 = urllib.parse.quote(key)
# print(value1)  # 你好 --> %E4%BD%A0%E5%A5%BD
url2 = f'https://tieba.baidu.com/f?ie=utf-8&kw={value1}'

# 3.解码
# unquote(字符串)  %E4%BD%A0%E5%A5%BD --> 你好
new = urllib.parse.unquote('%E4%BD%A0')
print(new)


