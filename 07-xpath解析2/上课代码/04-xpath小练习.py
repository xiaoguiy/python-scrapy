import pprint
html = '''
<!-- 第一本书 开始 -->
<book title="西游记" class="box-1 aa bb cc" index="01">
    <b class="book-1" href="https://www.###1.com" target="_parent">
        <a>《西游记》</a>
        </br>
        <a href="http://www.baidu.com">百度一下</a>
    </b>
    <img class="book1-img" id="ps-1" title="图片1" alt="img1.jpg"
        src="http://img3m6.ddimg.cn/54/26/28548486-1_b_19.jpg">
    <c class="xiaowu laowu">作者：<span>吴承恩</span></c>
    <d>今日<span>1000</span>人观看</d>
</book>
<!-- 第一本书 结束 -->
'''
from lxml import etree
html = etree.HTML(html)
# 1.今日1000人观看
d_tag = html.xpath('//book/d/text()')  # ['今日', '人观看']
span_tag = html.xpath('//book/d/span/text()')  # ['1000']
# 取的是d标签和d标签下的子节点文本内容
d_all_tag = html.xpath('//book/d//text()')  # ['今日', '1000', '人观看']
# print(''.join(d_all_tag))

# 2.获取book标签里所有的属性值
book_tag = html.xpath('//book/@*')
# print(book_tag)

# 3.获取book标签下所有标签的属性值
book_all_tag = html.xpath('//book//*/@*')  # 直属于
print(book_all_tag)


