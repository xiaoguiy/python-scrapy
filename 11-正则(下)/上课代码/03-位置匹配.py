import re
print(re.findall('6', '6dwj6jdbaj6'))  # ['6', '6', '6']
print(re.findall('^6', '6dwjjdbaj6'))  # 匹配以6开头的
print(re.findall('6$', 'dwjjdbaj6'))  # 匹配以6结尾的
