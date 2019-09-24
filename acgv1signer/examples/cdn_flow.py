 # -*- coding: utf-8 -*-  
 # 查询给定时间的流量
 # 文档地址：https://cloud.baidu.com/doc/CDN/s/5jwvyf8zn/#%E6%B5%81%E9%87%8F%E5%B8%A6%E5%AE%BD%E6%8E%A5%E5%8F%A3


import requests
from urllib.parse import urlparse
from acgv1signer import *
import json


if __name__ == '__main__':

    url = "http://cdn.baidubce.com/v2/stat/query"
    url_obj = urlparse(url)

    with open('key.txt', 'r') as f1:
        keys = f1.readlines()
    access_key = keys[0].strip('\n')
    secret_key = keys[1].strip('\n')

    credentials = BceCredentials(access_key,secret_key)

    http_method = "POST"
    path = url_obj.path
    headers1 = {
        "host": url_obj.netloc
    }
    params1 = None
    header_to_signs = ["host"]

    result = sign(credentials, http_method, path, headers1, params1, headers_to_sign=header_to_signs)

    headers = {
        "Authorization":result
    }

    datas = {
        "metric":"flow",
        "startTime":"2019-07-10T02:00:00Z",
        "endTime":"2019-07-18T05:00:00Z",
        #"key_type":2,
        "period":86400,
        "key":["cdn-galvin.e-galvin.cn"],
        "groupBy":"key"
       # "extra": 200
    }
    response = requests.post(url,data=json.dumps(datas),headers=headers)
    print(response.text,response.status_code)
