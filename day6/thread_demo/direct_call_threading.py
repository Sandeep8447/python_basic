# -*- coding:utf-8 -*-
__auth__ = 'christian'


import threading
import time


def sayhi(num):  # 定义每个线程要运行的函数

    print("running on number:%s" % num)

    time.sleep(3)


if __name__ == '__main__':
    # start_time = time.time()
    # t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
    # t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例
    #
    # t1.start()  # 启动线程
    # t2.start()  # 启动另一个线程
    #
    # t1.join()
    # #t2.join()
    #
    # print ('----------------')
    # print ('cost:', time.time() - start_time)
    #
    # print(t1.getName())  # 获取线程名
    # print(t2.getName())



    start_time = time.time()
    t_obj = []
    for i in range(50):
        t = threading.Thread(target=sayhi, args=('t-%s' % i, ))
        t.start()
        t_obj.append(t)

    for t in t_obj:
        t.join()

    print ('----------------')
    print ('cost:', time.time() - start_time)


