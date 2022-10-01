import requests
url = 'https://inv-veri.chinatax.gov.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
           }

# 像网站发生请求的时候 会自动检测数字证书 如果不想让他检测--> verify=False
res = requests.get(url, headers=headers, verify=False)
print(res.text)

