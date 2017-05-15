# -*- coding:utf-8 -*-
__auth__ = 'christian'


import threading
import time


def sayhi(num):  # 定义每个线程要运行的函数
    print("running on number:%s" % num)
    time.sleep(1)
    print ("task done", num)

if __name__ == '__main__':

    t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
    t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例

    t1.start()  # 启动线程
    t2.start()  # 启动另一个线程

    t1.join()
    t2.join()

    print ('----------------')

    print(t1.getName())  # 获取线程名
    print(t2.getName())



