# -*- coding:utf-8 -*-
__auth__ = 'christian'

# the communication between processes, multiprocess use the same queue.
# if using the Q2(threading queue) module, then different process use the different queue

from multiprocessing import Process, Queue
import Queue as Q2

def f(q,n):
    q.put([n, 'hello'])
    print q.get()
    print q.get()

def f2(q2,n):
    q2.put([n, 'world'])
    print q2.get()
    print q2.get()

if __name__ == '__main__':
    # you can find the result have five flag(s), copy five resources.
    q = Q2.Queue()
    q.put('flag')
    for i in range(5):
        p = Process(target=f, args=(q,i))
        p.start()

    # you can find only one flag.
    q2 = Queue()
    q2.put('flag_2')
    for j in range(5):
        p2 = Process(target=f2, args=(q2,j))
        p2.start()
        # while True:
        # print q.get()