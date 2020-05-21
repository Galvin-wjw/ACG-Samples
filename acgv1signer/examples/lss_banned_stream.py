import requests
from urllib.parse import urlparse
from acgv1signer import *

if __name__ == '__main__':

    url = "http://lss.bj.baidubce.com/v5/domain/galvin-hls.e-galvin.cn/app/test/stream/test2?pause"

    url_obj = urlparse(url)

    with open('key.txt', 'r') as f1:
        keys = f1.readlines()
    access_key = keys[0].strip('\n')
    secret_key = keys[1].strip('\n')

    credentials = BceCredentials(access_key,secret_key)

    http_method = "PUT"
    path = url_obj.path

    headers = {
        "host": url_obj.netloc
    }
    params = {
       "pause":None
    }

    header_to_signs = ["host"]
    result = sign(credentials, http_method, path, headers, params, headers_to_sign=header_to_signs)

    headers2 = {
        "Authorization":result
    }


    response = requests.put(url,headers=headers2)
    print(response.text,response.status_code)
