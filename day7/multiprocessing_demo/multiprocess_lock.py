# -*- coding:utf-8 -*-
__auth__ = 'christian'

from multiprocessing import Process, Lock
import time

# Process lock: Without using the lock output from the different processes is liable to get all mixed up.

def f(l, i):
    time.sleep(0.5)
    l.acquire()

    print 'hello world', i
    l.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(1000):
        Process(target=f, args=(lock, num)).start()