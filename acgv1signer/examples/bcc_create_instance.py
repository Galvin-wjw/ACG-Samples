import requests
from urllib.parse import urlparse
from acgv1signer import *
import json
import uuid


if __name__ == '__main__':

    # https://cloud.baidu.com/doc/BCC/s/yjwvyoe0s

    client_token = uuid.uuid1()
    url = "http://bcc.bj.baidubce.com/v2/instance?clientToken=" + str(client_token)
    url_obj = urlparse(url)

    with open('key2.txt', 'r') as f1:
        keys = f1.readlines()
    access_key = keys[0].strip('\n')
    secret_key = keys[1].strip('\n')

    credentials = BceCredentials(access_key,secret_key)

    http_method = "POST"
    path = url_obj.path
    headers1 = {
        "host": url_obj.netloc
    }
    params1 = {
        "clientToken":client_token
    }
    header_to_signs = ["host"]

    result = sign(credentials, http_method, path, headers1, params1, headers_to_sign=header_to_signs)

    headers = {
        "Authorization":result
    }

    datas = {
        "instanceType":"N3",
        "imageId":"m-RanvrTGP",
        "billing":{"paymentTiming":"Prepaid",
                   "reservation":{
                       "reservationLength":1
                   }},
        "cpuCount":1,
        "memoryCapacityInGB":4
    }
    response = requests.post(url,data=json.dumps(datas),headers=headers)
    print(response.text,response.status_code)
