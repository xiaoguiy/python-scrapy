def fun1():
    print('fun1')



print(__name__)  # 在别的模块运行 __name__的值就是test1
# 当在别的模块中导入了当前模块 我有内容不想被别的模块调用 可将不想调用的内容写到if下面
if __name__ == '__main__':  # 只有在自己当前这个模块运行name的值才是main
    fun1()
# fun1()