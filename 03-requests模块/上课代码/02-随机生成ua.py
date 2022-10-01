'''
pip install faker
'''
from faker import Faker  # 导入随机ua模块
f = Faker()  # 实例化对象
# 随机生成一个ua
# print(f.user_agent())

# 随机生成一个谷歌ua
print(f.chrome())

# 随机生成火狐ua
print(f.firefox())
