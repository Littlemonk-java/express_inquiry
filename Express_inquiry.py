# -*- coding: UTF-8 -*-
import cx_Oracle
import os
import requests,json
import random

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask, request

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def getcontent():
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
        "Connection":"keep-alive",
        "Cookie":"csrftoken=YubD3zQl11vCjEKP6sX12fJ7IVvL6AWqgxpYAy-tRKw; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1649206952; _adadqeqwe1321312dasddocTitle=kuaidi100; _adadqeqwe1321312dasddocReferrer=; _adadqeqwe1321312dasddocHref=; WWWID=WWW2B27155195638FE5528998620D355BC6; BAIDU_SSP_lcr=https://www.baidu.com/link?url=vDGVDrzPSEP5rrnKnZuQkKf3A28P_N1oU8mk-BvuRH358xLnQrcLi07nO1I1Bqn9&wd=&eqid=d195c04300632a6c00000003624ce6a2; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1649206961",
        "Host": "www.kuaidi100.com",
        "Referer":"https://www.kuaidi100.com/?from=openv",
        "sec-ch-ua": "'Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "'Windows'",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"

    }

    postid = request.values.get('postid')
    response = requests.post("https://www.kuaidi100.com/autonumber/autoComNum?text="+postid, headers=headers)
    typeReault = response.json()

    params = {
        'type': typeReault.get("auto")[0].get("comCode"),
        'postid': postid,
        'temp': "0."+random_number(18),
        'phone': ''
    }

    url = 'http://www.kuaidi100.com/query'

    res = requests.get(url, headers=headers, params=params)

    js = res.json()

    return json.dumps(js,ensure_ascii=False)

def random_number(num2):
    list2 = []
    for number in range(num2):
        str2 = str(random.randint(0, 9))
        list2.append(str2)
    b = " ".join(list2).replace(" ", "")
    return b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5590)