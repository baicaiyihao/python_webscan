#-*- encoding=utf-8 -*-

import requests
import time
import sys

url = 'http://www.jju.edu.cn'

def getHttpStatusCode(url):
    userAgent = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
    timeOut = 6
    try:
        request = requests.get(url, headers = userAgent, timeout = 6)
        httpStatusCode = request.status_code
        return httpStatusCode

    except requests.exceptions.HTTPError as e:
        return e

if __name__ == "__main__":
    status = getHttpStatusCode(url)
    print (status)