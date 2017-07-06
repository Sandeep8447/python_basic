# -*- coding:utf-8 -*-
__auth__ = 'christian'

# multiprocessing
# every processing starts a threading.

import multiprocessing
import threading
import time

def thread_run():
    print (threading._get_ident())

def f(name):
    time.sleep(2)
    print 'hello', name
    t = threading.Thread(target=thread_run,)
    t.start()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=f, args=('chris %s' %i,))
        p.start()