'''
没有拿到正确的数据-->当前页面是用户登录之后的 --> 没有登录信息-->携带cookie-->里面有我们的登录信息
cookie 时效性 (会过期)
'''
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
           'cookie': '_ga=GA1.2.1706990158.1644837134; pgv_pvid=2764259600; RK=FPcwOmkR2/; ptcz=b12029f8fbdd3782f6a7767e85b0bbbdcbf0502c46764cf60d3a9a758a022da0; sd_userid=25491646319577293; sd_cookie_crttime=1646319577293; tvfe_boss_uuid=e5385a75d4b52c5a; pt_sms_phone=150******64; fqm_pvqid=031500ea-1684-46e9-ab2a-74c1a582885c; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; pac_uid=0_80ff810b42968; luin=o3141750384; lskey=00010000fcf29138a13ac2f6d0543e23c6e3c10e0f1920117f8ee30108e7855af3ae4749e989b521ad55c698; _qpsvr_localtk=0.730559703804053; pgv_info=ssid=s2532410818; uin=o3141750384; skey=@MGI5dBwcN; p_uin=o3141750384; pt4_token=*q*HGi9PBa-F-9VHX6BMHc9spYuhDLNFwNLKC8LWYzw_; p_skey=1j2ql5*nMe-h-hKucCawZlNkasvT*bvtA*Tn*UP2ALU_; Loading=Yes; 3141750384_todaycount=0; 3141750384_totalcount=92; cpu_performance_v8=7'
           }
url = 'https://user.qzone.qq.com/3141750384'
response = requests.get(url, headers=headers)
print(response.text)


