from bs4 import BeautifulSoup
HTML = """
<a>
    <b>bbb</b><c>ccc</c><d>ddd</d>
</a>
"""
soup = BeautifulSoup(HTML, 'lxml')
# 1.next_sibling
# 获取b标签下一个兄弟节点
# print(soup.b.next_sibling)

# 2.previous_sibling
# 获取c标签上一个兄弟节点
# print(soup.c.previous_sibling)

# 3.next_siblings(生成器)
# 获取b标签下面所有兄弟节点
# print(list(soup.b.next_siblings))  # [<c>ccc</c>, <d>ddd</d>, '\n']

# 4.previous_siblings(生成器)
# 获取c标签上所有兄弟节点
print(list(soup.c.previous_siblings))  # [<b>bbb</b>, '\n']


