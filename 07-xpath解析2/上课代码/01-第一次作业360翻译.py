import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
           'pro': 'fanyi'}
url = 'https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=china'

eng = input('英译中 --> 1 中译英 --> 0')
key = input('请输入你要翻译的内容')
data_dict = {
    'eng': eng,
    'validate': '',
    'ignore_trans': '0',
    'query': key
}
response = requests.post(url, data=data_dict, headers=headers)
data = response.json()  # json对象--> python对象(字典)
print(data['data']['fanyi'])
print(type(data))

