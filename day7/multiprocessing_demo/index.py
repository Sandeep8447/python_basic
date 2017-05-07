# -*- coding:utf-8 -*-
__auth__ = 'christian'

# this script shows the the difference between the single and multiprocess effective.

from multiprocessing import Pool
import time
def f(n):
    time.sleep(2)
    return n*n

if __name__ == '__main__':
    p = Pool(5)
    a = [1,28,30,4,5]

    # multiprocess
    print (p.map(f, a))

    # single process
    print (map(f, a))