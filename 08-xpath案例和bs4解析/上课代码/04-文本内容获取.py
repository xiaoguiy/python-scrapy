from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story<title>岁岁在这</title></title></head>
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
# 1.string 获取当前标签中的文本内容
# title_text = soup.title.string

# 2.strings 获取多个标签的文本内容(获取当前节点下面子节点孙节点的文本内容) 返回结果是生成器
head_text = soup.head.strings
# print(head_text)  # <generator object Tag._all_strings at 0x00000264C1290F48>
# print(list(head_text))

# 3.stripped_strings 同上 但是会把多余的空格去掉 返回结果是生成器
body_text = soup.body.stripped_strings
body1_text = soup.body.strings
print(list(body_text))

'''
<a>我在这</a>
<b>我在这</b>
'''

'''
<a class="info">我在这<b>我在这</b></a>

'''

