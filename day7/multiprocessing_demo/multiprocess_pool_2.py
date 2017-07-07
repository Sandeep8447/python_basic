# -*- coding:utf-8 -*-
__auth__ = 'christian'

from  multiprocessing import Process, Pool, Lock
import time
import os

'''
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
'''

def Foo(i):
    time.sleep(2)
    print ("in process", os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg, os.getpid())


pool = Pool(5)

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)  #async

    # pool.apply(func=Foo, args=(i,))  # sync

print 'main process pid:', os.getpid()
print('end')
pool.close()
pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。