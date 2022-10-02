'''
去除空行:newline=''
注意:再次写入时先关闭文件
wps: utf-8  excel: utf-8-sig
'''
import csv  # 内置库 直接导入
li = [('岁岁', 21, 180), ('小爱', 100, 188)]
headers = ['name', 'age', 'height']  # 表头
# 普通写入 .txt
# for i in li:
#     # i表示列表的每一个元素
#     # i现在是一个元组
#     with open('a.txt', 'a', encoding='utf-8') as f:
#         # 创建文件对象
#         # 写入的数据类型必须是一个字符串
#         f.write(f'{i[0]},{i[1]},{i[2]}'+'\n')

# 方法1
with open('c.csv', 'w', encoding='utf-8', newline='') as f:
    # 创建文件对象f
    # 1.创建写入对象 传入文件对象
    # writer() --> [(),(),()]
    write = csv.writer(f)
    # 2.写入表头
    # writerow(序列) 写入单行
    write.writerow(headers)
    # 3.写入内容
    # for i in li:
    #     # i是元组
    #     write.writerow(i)
    # 3.1 写入多行
    write.writerows(li)


