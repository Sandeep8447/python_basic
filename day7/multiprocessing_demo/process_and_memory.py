# -*- coding:utf-8 -*-
__auth__ = 'christian'

from multiprocessing import Process
import threading
import time

# this script show the difference memory usage between process and thread.
# forking a process at the same time, a memory space gives to the process.
# so different process have its own memory space, but thread can not do this. A thread forked by a process, a process
# like a container can fork many threads, and all those threads can share the same memory space of the process.
#

def run_process(info_list, n):
    info_list.append(n)
    print info_list

def run_threading(info_list, n):
    info_list.append(n)
    print info_list

print '----Using process----'
info_1 = []
for i in range(10):
    p = Process(target=run_process, args=[info_1, i])
    p.start()


time.sleep(2)

print '----Using threading----'
info_2 = []
for j in range(10):
    p_2 = threading.Thread(target=run_threading, args=[info_2, j])
    p_2.start()

