'''
目标网站:https://fanyi.youdao.com/
需求: 小小的翻译软件 将用户输入的值翻译成英文或者中文
我们的数据是一直变化的 根据用户输入的值获取不同的结果
要翻译的内容根据我们的请求在作变化 我们需要携带上这些参数-->携带data
'''
import requests
# _o先删掉 涉及到js逆向
url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
key = input('请输入你要翻译的内容:')
data_dict = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16590118326408",
    "sign": "e4f98015c9536388e97ee803aa950749",
    "lts": "1659011832640",
    "bv": "f0819a82107e6150005e75ef5fddcc3b",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}
# 得到一个响应对象 赋值给response
response = requests.post(url, headers=headers, data=data_dict)

# text 返回的是str
# date = response.text
# print(date)
# print(type(date))

a = '{"name":"岁岁"}'  # --> json数据
# 使用之前先确定当前响应里的内容是json数据
# json() 把json数据-->python对象(字典)
date = response.json()  # 字典
# print(date, type(date))
print(date['translateResult'][0][0]['tgt'])  # [[{'src': 'hello', 'tgt': '你好'}]]



