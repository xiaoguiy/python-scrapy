'''
根据用户输入的关键字获取对应的页面
中国 https://tieba.baidu.com/f?ie=utf-8&kw=%E4%B8%AD%E5%9B%BD&fr=search
美女 https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BE%8E%E5%A5%B3&fr=search
游戏 https://tieba.baidu.com/f?ie=utf-8&kw=%E6%B8%B8%E6%88%8F&fr=search
kw = 用户搜索的关键字

翻页规律
周星驰第2页 https://tieba.baidu.com/f?kw=%E5%91%A8%E6%98%9F%E9%A9%B0&ie=utf-8&pn=50
周星驰第3页 https://tieba.baidu.com/f?kw=%E5%91%A8%E6%98%9F%E9%A9%B0&ie=utf-8&pn=100
周星驰第4页 https://tieba.baidu.com/f?kw=%E5%91%A8%E6%98%9F%E9%A9%B0&ie=utf-8&pn=150
pn = (当前页-1)*50
'''
import requests
key = input('请输入你要搜索的内容:')
start = int(input('请输入你的起始页:'))
end = int(input('请输入你的结束页:'))
# url是随着用户的输入的值有一直在变化
# 获取2-6页的内容
for i in range(start, end+1):
    print(i)  # 2 3 4 5 6
    # i表示页数 --> 根据页数构建url
    url = f'https://tieba.baidu.com/f?kw={key}&ie=utf-8&pn={(i-1)*50}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # print(response.text)
    # 获取数据 保存到本地
    # with open(文件名字.后缀名,读/写/追加,设置编码) as f:
    # 中国第2页.html 中国第3页
    with open(f'{key}第{i}页.html', 'w', encoding='utf-8') as f:
        # w r --> str
        f.write(response.text)



