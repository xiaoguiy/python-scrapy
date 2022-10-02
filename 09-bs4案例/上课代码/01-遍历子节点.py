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
# contents 获取所有子节点(返回结果是列表)
# print(soup.head.contents)

# children 获取一个标签的子节点 (返回结果是迭代器)
# print(soup.p.children)
# for n in soup.p.children:
#     print(n)

# descendants 获取标签下的子子孙孙节点(返回结果是生成器)
for i in soup.body.descendants:
    print(i)
    print('分割线')

