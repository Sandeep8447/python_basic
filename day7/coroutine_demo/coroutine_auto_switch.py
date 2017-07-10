# -*- coding:utf-8 -*-
__auth__ = 'christian'

from gevent import monkey
monkey.patch_all()

import gevent
from urllib import urlopen
import time

'''
协程， 协程gevent并发爬网页 
'''


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/'
        ]

time_start = time.time()
for url in urls:
    f(url)
print ("sync time:", time.time() - time_start)


async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print ("async time:", time.time() - async_time_start)