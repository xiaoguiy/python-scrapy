'''
pip install bs4
'''
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 实例化对象
# BeautifulSoup(网页源代码,解析器)
# 解析器 就是把html数据转化为soup对象的编码方法
soup = BeautifulSoup(html_doc, 'lxml')
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# 1.获取到一个标签以及标签中的内容(soup.标签名)
# soup.标签名 只会返回一个满足条件的标签 如果想返回多个--> find_all(标签名) 返回结果是列表
a_tag = soup.a
a_all_tag = soup.find_all('a')  # 列表
# print(a_all_tag)
# print(a_tag)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 2.获取标签名(soup.标签名.name) 比较鸡肋 我们就是根据标签名去获取标签下的内容
# print(soup.title.name)  # title

# 3.获取标签中的文本内容(soup.标签名.string)
title_text = soup.title.string
# print(title_text)

# 4.获取p标签的属性值
# 法1 标签名.get(属性名)
p_class = soup.p.get('class')  # ['title']
# 法2 标签名[属性名]
p1_class = soup.p['class']
# print(p1_class)

# 5.找一个不存在的标签 --> None
c_tag = soup.c
# print(c_tag)

