# -*- coding:utf-8 -*-
__auth__ = 'christian'


import requests

"""
IP地址归属地查询
"""
url = 'http://ip.cn/index.php?ip='
try:
    kv = {'user-agent': 'mozilla/5.0'}
    r= requests.get(url + '8.8.8.8', headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print r.content[-1000:]
except:
    print "爬取失败"