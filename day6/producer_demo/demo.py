# -*- coding:utf-8 -*-
__auth__ = 'christian'


from threading import Thread
from Queue import Queue
import time


class Producer(Thread):
    def __init__(self, name, queue):
        '''
        @param name: producer's name
        @param queue: container
        '''
        self.__Name = name
        self.__Queue = queue
        super(Producer, self).__init__()

    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('baozi')
                time.sleep(1)
                print '%s produces a baozi' %(self.__Name,)
        #Thread.run(self)


class Consumer(Thread):
    def __init__(self, name, queue):
        '''
        @param name: consumer's name
        @param queue: container
        '''
        self.__Name = name
        self.__Queue = queue
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get()
                time.sleep(1)
                print '%s consumer a baozi' %(self.__Name,)
        #Thread.run(self)

queue = Queue(maxsize=10)   # container
Proc1 = Producer('chris',queue)
Proc1.start()
Proc2 = Producer('scott',queue)
Proc2.start()
Proc3 = Producer('Ian',queue)
Proc3.start()

for item in range(3):
    name = "gameplayer%d" %(item,)
    temp = Consumer(name, queue)
    temp.start()


'''
print queue.qsize()
queue.put('1')
queue.put('2')
print 'empty:', queue.empty()
print queue.qsize()
print 'get:', queue.get()
print 'get:', queue.get()
print queue.qsize()
print 'empty:', queue.empty()
'''
