import urllib.request  # 内置库

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
url = 'https://www.baidu.com'
# 1.创建请求对象
res = urllib.request.Request(url, headers=headers)  # 请求对象
# urlopen函数不支持构建UA

# 2.获取响应对象
req = urllib.request.urlopen(res)  # urlopen可以传网址也可以传请求对象
# print(req.read())  # 字节数据类型

# 3.读取数据
print(req.read().decode('utf-8'))  # 手动的解码(字节-->字符串)

