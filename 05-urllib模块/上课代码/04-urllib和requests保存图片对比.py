# 1.用requests保存图片
# import requests
# # 右击 复制图片地址
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
# url = 'https://lmg.jj20.com/up/allimg/1114/0I120152936/200I1152936-4-1200.jpg'
# resposne = requests.get(url, headers=headers)
# # 图片的写入形式--> wb
# with open('tupian.png', 'wb') as f:
#     f.write(resposne.content)  # 以字节流的形式


# 2.用urllib模块保存图片
url = 'https://lmg.jj20.com/up/allimg/tp09/210F2130512J47-0-lp.jpg'
import urllib.request
# urlretrieve(图片地址, 图片命名)
urllib.request.urlretrieve(url, '2.jpg')

