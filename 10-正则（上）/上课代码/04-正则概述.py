# 常规写法 获取字符串中的数字
s = 'shidi33d6662bb99fff6d5'
for i in s:
    # 判断当前字符是不是一个数字 TF
    if i.isnumeric():
        print(i)

# 正则匹配
import re  # 内置 不需要下载
# findall(匹配规则,匹配内容)  返回形式是列表
res = re.findall('\d+',s)
print(res)


