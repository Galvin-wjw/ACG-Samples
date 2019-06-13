import requests
import json
from urllib.parse import urlparse
from bcev1signer import *

# 测试SMS发送短信接口：https://cloud.baidu.com/doc/SMS/API.html

if __name__ == '__main__':

    url = "http://sms.bj.baidubce.com/bce/v2/message"
    url_obj = urlparse(url)

    credentials = BceCredentials("XXXX", "XXXX")
    http_method = "POST"
    path = url_obj.path
    headers = {
        "host": url_obj.netloc
    }
    params = None
    header_to_signs = ["host"]
    result = sign(credentials, http_method, path, headers, params, headers_to_sign=header_to_signs)

    headers = {
        "Authorization":result
    }

    datas = {
        "invokeId": "-of3D-fr9A",
        "phoneNumber": "135",
        "templateCode": "smsTpl:e9d04ae900",
        "contentVar": {
            "others": "你好",
            "code": "7890"
        }
    }

    response = requests.post(url,headers=headers,data=json.dumps(datas))
    print(response.text,response.status_code)
