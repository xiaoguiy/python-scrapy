# 0.假设是我们获取的网页源代码
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """
# 1.导入
from lxml import etree
# 2.将我们的网页源代码转变成element对象
html = etree.HTML(wb_data)
# print(type(html))  # <class 'lxml.etree._Element'>
# 3.获取所有a标签的href属性值(获取属性值@)
# 先定位到a标签 再取值
# a_tag = html.xpath('//li/a')  # 将找到所有的a标签(标签对象)放到一个列表中
a_tag = html.xpath('//li/a/@href')
# print(a_tag)
# print(type(a_tag))  # <class 'list'>

# 4.获取所有a标签的文本内容(text())
text_tag = html.xpath('//li/a/text()')
# print(text_tag)

# 5.如果xpath没有获取到值会是一个空列表[]
a = html.xpath('//img')
# print(a)

# 6.当前div标签是根节点嘛? 不是
div_tag = html.xpath('/div')
# print(div_tag)  # [] 找不到
result = etree.tounicode(html)  # 自动补全网页格式(正常的网页结构都是从html标签开始)
# print(result)

# 7. 当前节点
li = html.xpath('//li')  # li是一个列表
for i in li:
    # i表示每一个li标签
    # i就表示当前节点 .--> 代表每一个li标签
    a = i.xpath('./a/text()')
    print(a)



