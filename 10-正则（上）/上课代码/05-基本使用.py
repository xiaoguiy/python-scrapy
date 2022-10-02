import re
# match(匹配规则, 匹配内容,可选 功能标识)
patter = 'hello'
s = 'hello and hi'
s1 = 'and hi'

# 如果匹配规则是一个普通的字符串(在正则没有特殊含义的符号)，在匹配内容中查询与自己相等的内容

# 根据我们的条件去匹配我们的数据 匹配到内容返回match对象 没有返回None
# print(re.match(patter, s))  # <re.Match object; span=(0, 5), match='hello'>返回的是match对象
# print(re.match(patter, s1))  # 没有匹配到内容返回None

# 查看匹配到的内容 match对象.group()
res = re.match(patter, s)
print(res.group())



