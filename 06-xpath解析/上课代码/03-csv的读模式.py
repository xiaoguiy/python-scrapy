import csv
# 法1
# with open('shuju.csv', 'r', encoding='utf-8') as f:
#     # 创建读取对象reader
#     read = csv.reader(f)
#     for i in read:
#         print(i)  # i是一个列表 csv文件里一行就是一个列表 ['苏苏', '21']


# 法2
with open('shuju.csv', 'r', encoding='utf-8') as f:
    # 创建读取对象DictReader
    read = csv.DictReader(f)
    for i in read:
        # i是字典 键值对
        print(i)  # OrderedDict([('name', '岁岁'), ('url', '20')])
        print(dict(i))  # {'name': '岁岁', 'url': '20'}
        # print(i['url'])  # 通过键取值




