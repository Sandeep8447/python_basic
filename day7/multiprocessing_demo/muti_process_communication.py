# -*- coding:utf-8 -*-
__auth__ = 'christian'

from multiprocessing import Process, Queue

# the communication between processes, multiprocess use the same queue.

def f(q, n):
    q.put([n, 'hello'])

if __name__ == '__main___':
    que = Queue()
    for i in range(5):
        p = Process(target=f, args=(que,i))
        p.start()
    while True:
        print que.get()
