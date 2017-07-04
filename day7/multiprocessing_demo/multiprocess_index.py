# -*- coding:utf-8 -*-
__auth__ = 'christian'

import multiprocessing
import time
def f(name):
    time.sleep(2)
    print ('hello', name)

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=f, args=('chris %s' %i,))
        p.start()