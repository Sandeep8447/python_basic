# -*- coding:utf-8 -*-
__auth__ = 'christian'

import requests
import os

"""
获取网络图片
"""
root = '/Users/hrgame/Pictures'
url = 'http://image.nationalgeographic.com.cn/2017/0823/20170823045853897.jpg'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print u"文件保存成功"
    else:
        print "文件已经存在"
except:
    print "爬取图片失败"