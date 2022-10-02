html_doc = """
<html><head><title>The Dormouse's story<b>The Dormouse's story</b></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
# 创建soup对象
soup = BeautifulSoup(html_doc, 'lxml')
# 找a标签
# print(soup.find('a'))  # 字符串过滤器
# print(soup.find(['a']))  # 列表过滤器

# find_all(标签名) 列表
# print(soup.find_all('a'))  # 找到所有的a标签

# 找到所有的a标签和title标签
# print(soup.find_all(['a', 'title']))

