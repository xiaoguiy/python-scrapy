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
# 1.获取title标签的父节点(返回标签对象)
# print(soup.title.parent)

# 2.html有父节点嘛？
# 顶级节点html的父节点是bs4对象
# print(type(soup.html.parent))  # <class 'bs4.BeautifulSoup'>

# 3.获取title标签所有的父节点(返回结果是生成器)
for i in soup.title.parents:
    # print(i)  # 父节点
    print(i.name)
    # [document]--> bs4对象



