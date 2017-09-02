# -*- coding:utf-8 -*-
__auth__ = 'christian'

import requests

def getHtmlContent(url):
    try:
        r = requests.get(url,  timeout=30)
        r.raise_for_status()
        print r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'something wrong!!'


if __name__ == '__main__':
    url = 'https://www.duanlian.tech'
    result = getHtmlContent(url)
    print result