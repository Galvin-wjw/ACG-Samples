import requests
from urllib.parse import urlparse
from bcev1signer import *
import datetime
import json

if __name__ == '__main__':
    url = "http://rds.bj.baidubce.com/v1/instance"

    url_obj = urlparse(url)

    with open('key.txt', 'r') as f1:
        keys = f1.readlines()

    access_key = keys[0].strip('\n')
    secret_key = keys[1].strip('\n')

    credentials = BceCredentials(access_key, secret_key)

    http_method = "GET"
    path = url_obj.path
    #now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    headers1 = {
        "host": "rds.bj.baidubce.com"
    }

    params1 = None
    header_to_signs = ["host"]
    result = sign(credentials, http_method, path, headers1, params1, headers_to_sign=header_to_signs)

    headers = {
        "Authorization": result
    }

    response = requests.get(url=url, headers=headers)
    print(json.dumps(response.text), response.status_code)
