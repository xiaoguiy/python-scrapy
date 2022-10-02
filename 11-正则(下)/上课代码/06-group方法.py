import re
s = '123abc678'
# group()和group(0)返回整个匹配到的文本
# group(1)返回第一个括号中匹配到的内容
# group(2)返回第二个括号中匹配到的内容
# groups()返回一个包含所有子串的元组
# print(re.search('[0-9]*[a-z]*[0-9]*', s).group())  # 123abc678
# print(re.search('[0-9]*[a-z]*[0-9]*', s).group(0))  # 123abc678
print(re.search('([0-9]*)([a-z]*)([0-9]*)', s).group(1))  # 123
print(re.search('([0-9]*)([a-z]*)([0-9]*)', s).group(2))  # abc
print(re.search('([0-9]*)([a-z]*)([0-9]*)', s).group(3))  # 678
print(re.search('([0-9]*)([a-z]*)([0-9]*)', s).groups())  # ('123', 'abc', '678')
