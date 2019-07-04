import requests
from urllib.parse import urlparse
from bcev1signer import *
import datetime

if __name__ == '__main__':
    url = "http://rds.bj.baidubce.com/v1/instance/rds-T65y9mic?reboot"

    url_obj = urlparse(url)

    with open('key.txt', 'r') as f1:
        keys = f1.readlines()

    access_key = keys[0].strip('\n')
    secret_key = keys[1].strip('\n')

    credentials = BceCredentials(access_key, secret_key)

    http_method = "PUT"
    path = url_obj.path

    headers1 = {
        "host": url_obj.netloc
    }

    params1 = {"reboot":None}
    header_to_signs = ["host"]
    result = sign(credentials, http_method, path, headers1, params1, headers_to_sign=header_to_signs)

    now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    headers = {
        "Authorization": result
    }

    response = requests.put(url=url, headers=headers)
    print(response.text,response.status_code)
