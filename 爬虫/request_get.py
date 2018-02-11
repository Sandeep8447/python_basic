# -*- coding:utf-8 -*-
__auth__ = 'christian'

import requests

def getHtmlContent(url):
    try:
        kv = {'user-agent': 'mozilla/5.0'}  # modify the http header for the python-requests
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        print r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'something wrong!!'


if __name__ == '__main__':
    url = 'http://httpbin.org'
    result = getHtmlContent(url)
    print result