import re
s = """
<div class="panel panel-default">岁岁在这</div>
<div class="panel-heading">本周热点</div>
<li class="title">不要提取我...</li>  
<div class="panel-body">我是第三个个div</div>  
<!-- List group -->  
<ul class="list-group">    
	<li class="list-group-item">三门峡市陕州区一中餐厅管理工作...</li>   
	<li class="list-group-item">鹤壁七中多措并举助推"六城联创...</li>    
	<li class="list-group-item">沙溪中学开展"扫黑除恶"专项宣...</li> 
	<li class="list-group-item">中牟县晨阳路学校："点缀生活 ...</li>  
	<li class="list-group-item">上饶市第二保育院开展预防手足口...</li>  
</ul>
"""
# 1.获取所有div标签
div_tag = re.findall('<div.*?>(.*?)</div>', s, re.S)
# print(len(div_tag))
# print(div_tag)

# 2.获取ul标签
ul_tag = re.findall('<ul class="list-group">.*</ul>', s, re.S)
# print(ul_tag)

# 3.获取所有li标签中的文本内容
li_tag = re.findall('<li.*?>(.*?)</li>', s, re.S)
for i in li_tag:
    print(i)

    



