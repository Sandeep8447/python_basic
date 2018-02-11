# -*- coding:utf-8 -*-
__auth__ = 'christian'

import requests

"""
使用百度搜索某个关键字并获取搜索结果
"""
keyword = "Python"
try:
    kv = kv = {'k': 'v', 'x': 'y'}
    r = requests.get('https://www.baidu.com/s', params=kv)
    print r.request.url
    r.raise_for_status()
    print len(r.text)
except:
    print  u"爬取失败"