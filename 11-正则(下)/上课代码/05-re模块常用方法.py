import re
# 事先把通用的匹配规则定义好 可以重复的使用
# 创建模板对象compile(正则表达式)
pat = re.compile('abc')
res = pat.match('abc123')
# print(res)  # <re.Match object; span=(0, 3), match='abc'>

# search()查找的位置不用固定到开头 返回第一个匹配到的对象
# search和match区别：
# match如果开头就不和正则表达式匹配直接返回None 而search是匹配整个字符串(在整个字符串中进行检索)
# print(re.match('abc', '123abc123abc'))  # None
# print(re.search('abc', '123abc123abc').group())  # abc


# 如果想不看位置并且想返回所有多个满足规则 --> findall()返回结果是个列表(不是match对象 不能用group方法)
# print(re.findall('abc', '123abc123abc'))  # ['abc', 'abc']

# sub 类型replace 可以把多种不同类型的字符统一替换(删除)
s = '《战狼》'
# 普通字符串replace(老的,新的)
# print(s.replace('《', '').replace('》', ''))

# re.sub(匹配规则, 新的, 做替换的字符串)
# print(re.sub('[《》]', '', s))

# split(匹配规则,字符串对象)
ss = '7+2-5*8/9'
# print(re.split('[\+\-\*\/]', ss))


# re.I 不区分大小写(不敏感)
pat = re.compile('abc', re.I)
# print(pat.match('ABC'))  # ABC

# re.S 匹配换行以内的字符
s1 = """静夜思
床前明月光
疑是地上霜
举头望明月
低头思故乡
"""

print(re.match('.*', s1))  # 静夜思
print(re.match('.*', s1, re.S).group())  # 静夜思





