# -*- coding:utf-8 -*-
__auth__ = 'christian'

from multiprocessing import Process, Queue

# queue

def f(q, n):
    q.put([n, 'hello'])

if __name__ == '__main___':
    print 'start'
    q = Queue()
    for i in range(5):
        print i
        p = Process(target=f, args=(q, i))
        p.start()
    while True:
        print q.get()
