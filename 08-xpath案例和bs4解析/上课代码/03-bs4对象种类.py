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
soup = BeautifulSoup(html_doc, 'lxml')
# 1.tag 标签 获取的是标签和标签中的内容
a_tag = soup.a
# print(type(a_tag))  # <class 'bs4.element.Tag'>

# 2.bs4对象 我们一直在用这个方法去创建一个对象
# print(type(soup))  # <class 'bs4.BeautifulSoup'>

# 3. NavigableString 提取内容 获取的是标签中的数据
b_tag_string = soup.b.string
# print(type(b_tag_string))  # <class 'bs4.element.NavigableString'>


html = """
<a><!--岁岁!--></a>
"""
# 4.Comment 如果获取的标签中的内容是一个注释返回的是comment对象
soup1 = BeautifulSoup(html, 'lxml')
atag = soup1.a.string
print(atag)  # 岁岁!
print(type(atag))  # <class 'bs4.element.Comment'>

