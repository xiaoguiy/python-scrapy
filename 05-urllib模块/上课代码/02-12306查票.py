'''
目标网站:https://www.12306.cn/index/
需求:获取8.3号的 车次(3) 商务座(32) 一等座(31) 二等座(30)
'''
import pprint

import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
           ,'Cookie': '_uab_collina=165347901561124946500772; JSESSIONID=19BA64ED3E8054253485512FD074578A; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_wfdc_flag=dc; BIGipServerotn=1557725450.24610.0000; BIGipServerpassport=820510986.50215.0000; highContrastMode=defaltMode; guidesStatus=off; cursorStatus=off; RAIL_EXPIRATION=1659509866159; RAIL_DEVICEID=PPYbojIx5C2_aXfqrNYPVU46ckzTpdfr-qUFHX6ImDSd4XnrdPnZC9Ye-RrG-Q2BSO9SU1c2LQ8c3nOGq9wokIQ1gqFJILI1ZYDi4yRfDbBaoPahWYDnVFnK9jnpUKCMul7ld4r5wHF3xLePzZP2WatB3dBuDsE-; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toStation=%u91CD%u5E86%2CCQW; _jc_save_toDate=2022-07-30; BIGipServerportal=3084124426.17183.0000; _jc_save_fromDate=2022-08-11'}

# 被反爬了 加cookie cookie中记录了我们访问页面的时间
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-08-11&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CQW&purpose_codes=ADULT'
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
data = res.json()  # data转换之后是一个字典
# 确保拿到数据之后再作转换
# print(data)
# pprint.pprint(data) 输出让数据有层级关系 方便查看
li = data['data']['result']  # 列表
for i in li:
    li_res = i.split('|')  # spilt函数的返回结果列表
    print(f'车次:{li_res[3]},商务座:{li_res[32]},二等座:{li_res[31]},一等座:{li_res[30]}')
    # i代表每一个车次的信息
    # print(i)
    # break
    # for k, j in enumerate(li_res):
    #     print(k, j)
