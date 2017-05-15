# -*- coding:utf-8 -*-
__auth__ = 'christian'


import threading
import time

def sayhi(n):  # 定义每个线程要运行的函数
    global num
    time.sleep(5)
    num += 1

if __name__ == '__main__':

    num = 0
    t_obj = []  # 存线程实例
    for i in range(1000):
        t = threading.Thread(target=sayhi, args=('t-%s' % i, ))
        t.start()
        t_obj.append(t)  # 为了不阻塞后面的线程启动，不在这里使用join方法，先存放到一个列表里

    for t in t_obj:  # 循环线程实例表，等待所有线程执行完毕
        t.join()

    print ('--------all threads have finished.--------')
    print (threading.current_thread(),threading.active_count())

    time.sleep(2)
    print ('num:', num)  # num不等于100

# --------all threads have finished.--------
# (<_MainThread(MainThread, started 139625935087360)>, 1)
# ('num:', 987)


