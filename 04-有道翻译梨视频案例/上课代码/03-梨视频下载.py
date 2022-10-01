'''
目标网站:https://www.pearvideo.com/
需求: 将视频下载到本地
'''
import requests
r_url = input('请输入你的下载链接:')
# 提取id
id = r_url.split('_')[1]  # 1756772
# print(id)
url = f'https://www.pearvideo.com/videoStatus.jsp?contId={id}&mrd=0.46545587792333665'
# print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
           'Referer': r_url
           }
# 加上referer参数 代表从哪个页面跳转过来
response = requests.get(url, headers=headers)
# data是个字符串
data = response.json()
# print(data)
print('*'*100)
# print(type(data), data)
# 先拿到响应里的链接
url_res = data['videoInfo']['videos']['srcUrl']
# print(url_res)

# 提取时间戳
systemTime = data['systemTime']
# print('时间戳', systemTime)
# 进行替换拿到真正的url
true_url = url_res.replace(systemTime, f'cont-{id}')
print(true_url)

result = requests.get(true_url, headers=headers)
# 图片视频的保存 --> 以字节流的形式写入 wb
with open('shipin.mp4', 'wb') as f:
    # 写入的数据内容是字节类型
    f.write(result.content)




