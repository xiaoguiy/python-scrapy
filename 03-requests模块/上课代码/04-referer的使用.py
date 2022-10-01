'''
比如我们只想我自己的网站去访问我服务器里的图片 那么我可以拿他的referer去判断 如果是www.baidu.com
就说明是自己网站访问的 就运行访问 如果不是  就拦截
日本人去南京？ 国籍不是中国--> 拦截
梨视频 获取视频的下载链接
'''
import requests
url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1760318&mrd=0.5445625983123952'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
           'Referer': 'https://www.pearvideo.com/video_1760318'
           }
response = requests.get(url, headers=headers)
print(response.text)



