import requests
import json
from urllib.parse import urlparse
from acgv1signer import *


if __name__ == '__main__':

    url = "http://sts.bj.baidubce.com/v1/sessionToken"
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
    params = None
    header_to_signs = ["host"]
    result = sign(credentials, http_method, path, headers1, params, headers_to_sign=header_to_signs)

    headers = {
        "Authorization":result,
        "Content-type": "application/json"
    }

    datas = {
        "accessControlList":[ {
            "effect": "Allow",
            "permission": ["READ"],
            "region":"*",
            "resource":["test316/*"],
            "service":"bce:bos"
        }]
    }

    response = requests.post(url,headers=headers,data=json.dumps(datas))
    print(response.text,response.status_code)
