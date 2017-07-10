# -*- coding:utf-8 -*-
__auth__ = 'christian'

import gevent

'''
The difference between synchronous and asynchronous
程序的重要部分是将task函数封装到Greenlet内部线程的gevent.spawn。 初始化的greenlet列表存放在数组threads中，此数组被传给gevent.joinall 
函数，后者阻塞当前流程，并执行所有给定的greenlet。执行流程只会在 所有greenlet执行完后才会继续向下走。
'''

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()