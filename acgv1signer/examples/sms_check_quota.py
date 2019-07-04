import requests
from acgv1signer import *

# 测试SMS发送短信配额接口：https://cloud.baidu.com/doc/SMS/API.html

if __name__ == '__main__':

    credentials = BceCredentials("XXXXXX", "XXXXXX")
    host = "sms.bj.baidubce.com"
    http_method = "GET"
    path = "/v1/quota"
    headers = {
        "content-type": "application/json",
        "host": "sms.bj.baidubce.com"
    }
    params = None
    header_to_signs = ["host", "content-type"]
    result = sign(credentials, http_method, path, headers, params, headers_to_sign=header_to_signs)

    headers = {
        "Host":host,
       "Content-Type":"application/json",
        "Authorization":result
    }

    url = "http://" + host + path
    response = requests.get(url=url,headers=headers)
    print(response.text,response.status_code)
    print(response.headers)
