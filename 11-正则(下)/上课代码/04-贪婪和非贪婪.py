'''
贪婪就是尽量往多的匹配 比如+
贪婪就是尽量往少的匹配
正则中默认就是贪婪匹配
?非贪婪模式标志 进行最小匹配 前一个规则出现0次或者1次
'''
import re
s = '<a>123</a><a>678></a>'
# .* 匹配到的是 123</a><a>678>
pnt = '<a>.*</a>'  # 只要字符串中的内容满足规则 就会全部匹配少
pnt1 = '<a>.*?</a>'  #
print(re.match(pnt, s))  # <a>123</a><a>678></a>
# .*?匹配到的是123
print(re.match(pnt1, s))  # <a>123</a>


# print(re.match('ab+', 'abbbc'))  # 贪婪匹配 abbb
# print(re.match('ab+?', 'abbbc'))  # 非贪婪匹配 abbb

print(re.match('\d+', '20220813'))
print(re.match('\d+?', '20220813'))
