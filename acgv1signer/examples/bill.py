import requests
from urllib.parse import urlparse
from acgv1signer import *


if __name__ == '__main__':

    url = "http://billing.baidubce.com/v1/bill/resource/month?month=2019-04&productType=prepay"
    url_obj = urlparse(url)

    with open('key.txt', 'r') as f1:
        keys = f1.readlines()
    access_key = keys[0].strip('\n')
    secret_key = keys[1].strip('\n')

    credentials = BceCredentials(access_key,secret_key)

    http_method = "GET"
    path = url_obj.path
    headers1 = {
        "host": url_obj.netloc
    }
    params1 = {
        "month":"2019-04",
        "productType":"prepay"
    }
    header_to_signs = ["host"]
    result = sign(credentials, http_method, path, headers1, params1, headers_to_sign=header_to_signs)

    headers = {
        "Authorization":result
    }


    response = requests.get(url,headers=headers)
    print(response.text,response.status_code)
