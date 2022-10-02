import csv
item = [{'name': '岁岁', 'url': 20},
        {'name': '小爱', 'url': 20},
        {'name': '苏苏', 'url': 21}]

with open('shuju3.csv', 'w', encoding='utf-8', newline='') as f:
    # 1.创建写入对象
    # fieldnames=[] 指定表头
    # 表头名字和字典里的键一定要一致
    # 我们是根据字典里面的键去寻找对应的表头名字 如果没有 则报错
    # DictWriter() --> [{}，{}，{}]
    write = csv.DictWriter(f, fieldnames=['name', 'url'])
    # 2.将表头写入
    write.writeheader()
    # 3.写入数据(一次性写入)
    write.writerows(item)

