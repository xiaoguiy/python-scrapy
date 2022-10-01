'''
str 字符串 给我们看 用来操作
bytes 字节 给计算机看 用于计算机传输 图片视频的下载
'''
# str--> bytes
# s = 'hello'
# s1 = s.encode()
# print(s1, type(s1))  # b'hello' <class 'bytes'>

# bytes--> str
s2 = b'shs'
s3 = s2.decode()
print(s3, type(s3))  # shs <class 'str'>

