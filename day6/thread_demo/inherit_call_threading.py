# -*- coding:utf-8 -*-
__auth__ = 'christian'

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num, sleep_time):
        threading.Thread.__init__(self)
        self.num = num
        self.sleep_time = sleep_time

    def run(self):  # 定义每个线程要运行的函数
        print("running on number:%s" % self.num)
        time.sleep(self.sleep_time)
        print ('task %s done' % self.num)


if __name__ == '__main__':
    t1 = MyThread('t1', 2)
    t2 = MyThread('t2', 4)
    t1.start()
    t2.start()

    t1.join()
    #t2.join()

    print '---main thread---'