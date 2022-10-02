# 单线程下载
# import time
# import requests
#
# url_list = [('车', 'https://video.pearvideo.com/mp4/short/20220713/cont-1750967-15905855-hd.mp4'),
#             ('上海人吃瓜', 'https://video.pearvideo.com/mp4/adshort/20220524/cont-1763204-15884803_adpkg-ad_hd.mp4'),
#             ('生活', 'https://video.pearvideo.com/mp4/adshort/20220617/cont-1765616-15897269_adpkg-ad_hd.mp4')]
#
# print(time.time())  # 下载前的时间
# for name, url in url_list:
#     response = requests.get(url)
#     with open(f'{name}.mp4', 'wb') as f:
#         f.write(response.content)
# print(time.time())  # 下载完成之后的时间

# 多线程
import time
import requests
import threading

url_list = [('车', 'https://video.pearvideo.com/mp4/short/20220713/cont-1750967-15905855-hd.mp4'),
            ('上海人吃瓜', 'https://video.pearvideo.com/mp4/adshort/20220524/cont-1763204-15884803_adpkg-ad_hd.mp4'),
            ('生活', 'https://video.pearvideo.com/mp4/adshort/20220617/cont-1765616-15897269_adpkg-ad_hd.mp4')]

def task(name,url):
    response = requests.get(url)
    with open(f'{name}.mp4', 'wb') as f:
        f.write(response.content)
        print('下载中', time.time())

print('开始',time.time())

for name, url in url_list:  # 创建三个线程
    t1 = threading.Thread(target=task, args=(name, url))
    t1.start()

print('好')
