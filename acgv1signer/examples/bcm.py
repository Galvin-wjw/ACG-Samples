import requests
from urllib.parse import urlparse
from bcev1signer import *

if __name__ == '__main__':

    url = "http://bcm.bj.baidubce.com/json-api/v1/metricdata/f2205b52fe1a46d5bb69b271bf88603d/BCE_BCC/vCPUUsagePercent?" \
          "dimensions=InstanceId:5a972503-cfec-4213-9daf-9ee5f19343b8" \
          "&statistics[]=average" \
          "&periodInSecond=60" \
          "&startTime=2019-05-30T13:00:01Z" \
          "&endTime=2019-05-30T13:10:01Z"

    url_obj = urlparse(url)

    with open('key.txt', 'r') as f1:
        keys = f1.readlines()
    access_key = keys[0].strip('\n')
    secret_key = keys[1].strip('\n')

    credentials = BceCredentials(access_key,secret_key)

    http_method = "GET"
    path = url_obj.path

    headers = {
        "host": url_obj.netloc
    }
    params = {
        "dimensions":"InstanceId:5a972503-cfec-4213-9daf-9ee5f19343b8",
        "endTime":"2019-05-30T13:10:01Z",
        "periodInSecond":60,
        "startTime": "2019-05-30T13:00:01Z",
        "statistics[]":"average"
    }

    header_to_signs = ["host"]
    result = sign(credentials, http_method, path, headers, params, headers_to_sign=header_to_signs)

    headers2 = {
        "Authorization":result
    }


    response = requests.get(url,headers=headers2)
    print(response.text,response.status_code)
