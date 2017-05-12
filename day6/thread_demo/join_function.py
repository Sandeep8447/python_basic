# *_*coding:utf-8 *_*
__auth__ = 'christian'

import threading
import time

#  主线程A中，创建了子线程B，并且在主线程A中调用了B.join()，那么，主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，
#  那么在调用这个线程时可以使用被调用线程的join方法。
#  原型：join([timeout])
#  里面的参数时可选的，代表线程运行的最大时间，即如果超过这个时间，不管这个此线程有没有执行完毕都会被回收，然后主线程或函数都会接着执行的。

class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        x = 0
        time.sleep(10)
        print self.id


if __name__ == "__main__":
    t1 = MyThread(999)
    t1.start()
    # 线程t1 start后，主线程并没有等线程t1运行结束后再执行，而是主线程和线程t1同时开始执行把, 主线程5次循环打印执行完毕（打印到4）
    # 线程t1sleep（10）后，线程t1把传进去的999才打印出来。
    for i in range(5):
        print i

    t2 = MyThread(999)
    t2.start()
    t2.join()   # 线程t2 start后，主线程停在了join()方法处，等sleep（10）后，线程t2操作结束被join，接着，主线程继续循环打印。
    for j in range(5):
        print j