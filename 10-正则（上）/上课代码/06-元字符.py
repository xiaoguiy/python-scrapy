import re
# 1.除开换行(\n) 别的都能匹配到(匹配一个字符)
# print(re.match('a.cde', 'a3cde'))  # a3cde
# print(re.match('a.cde', 'a岁cde'))  # a岁cde
# print(re.match('a.cde', 'a平安cde'))  # .只能匹配到'平' '安'字匹配不到 None
# print(re.match('a.cde', 'a\ncde'))   # None

# 2 | 逻辑或 (匹配a或者匹配b 谁先找到就返回谁)
# print(re.match('a|b', 'a'))  # a
# print(re.match('a|b', 'b'))  # b
# print(re.match('a|b', 'ab'))  # a 匹配到第一个数据 直接返回
# print(re.match('a|b', 'ca'))  # None 在a和b里没有找到c 直接返回None 匹配数据第一个没有匹配到 后面的不会再看


# 3 [] 匹配字符集里的一个内容(只要匹配内容在字符集中 就能匹配到)
# print(re.match('[345abc]', '3'))  # 3
# print(re.match('[345abc]', 'a'))  # a
# print(re.match('[345abc]', '3a'))  # 3  找到直接返回 后面的不管
# [345abc]a --> 两个匹配规则 第一个是字符集中的 第二个是个普通的字符串
# print(re.match('[345abc]a', '3a'))  # 3a
# print(re.match('[345abc]a', '3'))  # None a也是一个匹配规则 必须带上


# 4 [^] 对字符集取反(只要不在字符集中的内容 都能匹配到)(^必须放到字符集的最前面)
# print(re.match('[^21期爬虫]', '666'))  # 6


# 5 -范围
# print(re.match('[a-z]', 'y'))  # y
# print(re.match('[a-z]', 'ya'))  # y
# print(re.match('[A-Z]', 'ya'))  # None
# print(re.match('[0-9]', '3'))  # 3
# [0-10] 不是0-10  是0-1
# print(re.match('[0-10]', '5'))  # None
# [爬-虫]只能匹配'爬'和'虫'
# print(re.match('[爬-虫]', '岁'))  # None


# 6 \ 对后面的字符转义
# print('\n')
# 如果只是想单单输出\n这个字符串
# print('\\n')
# print(r'\n')

# 本来.是有特殊含义(匹配所有除开换行)的 在前面加上一个\进行转义之后 不再拥有特殊含义 只是一个普通的.
# print(re.match('哈利\.波特', '哈利的波特'))  # None

# ?(有特殊含义)表达式出现0次或者一次
print(re.match('你在干嘛?', '你在干嘛?'))  # 你在干嘛
print(re.match('你在干嘛\?', '你在干嘛?'))  # 你在干嘛?







