# -*- coding:utf-8 -*-
__auth__ = 'christian'

'''
A manager object returned by Manager() controls a server process which holds Python objects and allows other processes 
to manipulate them using proxies.

A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, 
Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array.
'''
from multiprocessing import Process, Manager
import os

def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  # generate a dictionary, can be shared in different processes.
        l = manager.list(range(5))  # generate a list, can be shared in different processes.
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)