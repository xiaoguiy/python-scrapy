import re
# 1.\d 匹配0-9之间的数字
# print(re.match('\d', '725'))  # 7

# 2.\w 匹配数字字母下划线汉字
# print(re.match('\w','32gA'))  # 3
# print(re.match('\w','A2gA'))  # A
# print(re.match('\w','c2gA'))  # c
# print(re.match('\w','_dhd'))  # _下划线
# print(re.match('\w','中国'))  # 中

# 3.\s 匹配空格 换行
# print(re.match('\s', ''))  # None
# print(re.match('\s', ' '))
# print(re.match('\sa', ' a'))

# 4.\D 匹配非数字
# print(re.match('\D', 'e'))  # e
# [^\d]等价于\D 不是数字 都能匹配到
# print(re.match('[^\d]', '@'))  # @

# 5.\W 匹配非数字字母下划线汉字(匹配特殊符号)
# print(re.match('\W', '*'))
# print(re.match('\W', '/'))
# print(re.match('\W', '#'))

# 6.\S 匹配非空白
# print(re.match('\S', ' '))  # None
# print(re.match('\S', 'han'))  # None








