import re
# 1.{n} 表达式匹配n次(固定重复n次)
# \d这个表达式出现三次
# print(re.match('\d{3}', '20'))  # None
# print(re.match('\d{3}', '202'))  # 202
# print(re.match('\d{3}', '2022'))  # 202

# 2.{m, n} 表达式至少重复m次 最大重复n次 >=2  <=5
# print(re.match('\d{2,5}', '1'))  # None
# print(re.match('\d{2,5}', '12'))  # 12
# print(re.match('\d{2,5}', '123'))  # 123
# print(re.match('\d{2,5}', '123666'))  # 12366

# 3.{m,} 至少重复m次 有下限  没有上限
# print(re.match('\d{3,}', '23'))  # None
# print(re.match('\d{3,}', '234'))  # 234
# print(re.match('\d{3,}', '234566784'))  # 234566784

# 4.?表达式出现0次或者1次(不能匹配多次) ?前面的表达式要么不出现 要么只出现一次
# print(re.match('a[a-z]', 'a'))  # None
# print(re.match('a[a-z]?', 'a'))  # a
# print(re.match('a[a-z]?', 'acd'))  # ac

# 5.+ 表达式至少出现一次(无限次) 就是最少一次 >=1
# [a-z]+ 代表[a-z]至少要匹配一次 如果没有匹配 None
# print(re.match('a[a-z]+', 'a'))  # None
# print(re.match('a[a-z]+', 'aa'))  # aa
# print(re.match('a[a-z]+', 'aewer'))  # aewer

# 6.*表达式出现0次或者任意次(无限次) 可有可无 出现就匹配 >=0
print(re.match('a[a-z]', 'ac'))  # ac
print(re.match('a[a-z]*', 'acqq'))  # acqq
print(re.match('a[a-z]*', 'a'))  # a
