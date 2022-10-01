'''
Query String Parameters: 一般就是我们目标url中的参数
Form Date :一般是post请求需要携带上的参数
'''
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

url = 'https://www.baidu.com/s?'

params_dict = {
    "ie":"utf-8",
    "f":"8",
    "rsv_bp":"1",
    "rsv_idx":"1",
    "tn":"baidu",
    "wd":"python",
    "fenlei":"256",
    "rsv_pq":"97ca2cc2000b29b0",
    "rsv_t":"c58e4W1ev3dnvOkyhKo+cS8gpZBfe8v6DE7AErBTWv2FuZx/SghJ4ORxVe48",
    "rqlang":"en",
    "rsv_enter":"1",
    "rsv_dl":"tb",
    "rsv_sug2":"0",
    "rsv_btype":"i",
    "inputT":"1945",
    "rsv_sug4":"2645",
}
# 如果需要对url进行调整可能不是很方便 后面一部分的查询参数可以单独拿出来构建
# params 用来完善目标url 不区分get还是post
response = requests.get(url, headers=headers, params=params_dict)
print(response.text)
