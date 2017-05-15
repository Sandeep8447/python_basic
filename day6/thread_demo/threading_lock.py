# -*- coding:utf-8 -*-
__auth__ = 'christian'


import threading
import time

# python GIL bug
# apply threading lock

def sayhi(n):  # 定义每个线程要运行的函数
    global num  # 每个线程中都获取这个全局变量
    lock.acquire()  # 修改数据前加锁
    num += 1
    # time.sleep(1)  # sleep 后直接导致执行方式变成串行， sleep的时间1秒threading lock 没有被释放
    lock.release()  # 修改数据后释放

if __name__ == '__main__':

    lock = threading.Lock()  # 生成全局锁
    num = 0  # 设定一个共享变量
    t_obj = []  # 存线程实例
    for i in range(50):
        t = threading.Thread(target=sayhi, args=('t-%s' % i, ))
        t.start()
        t_obj.append(t)  # 为了不阻塞后面的线程启动，不在这里使用join方法，先存放到一个列表里

    for t in t_obj:  # 循环线程实例表，等待所有线程执行完毕
        t.join()

    print ('--------all threads have finished.--------')
    print (threading.current_thread(),threading.active_count())

    time.sleep(2)
    print ('num:', num)



