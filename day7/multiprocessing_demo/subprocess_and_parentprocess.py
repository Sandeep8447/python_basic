# -*- coding:utf-8 -*-
__auth__ = 'christian'

from multiprocessing import Process
import os
import time

'''
In Unix-like operating systems, every process except process 0 (the swapper) is created when another process
executes the fork() system call. The process that invoked fork is the parent process and the newly created process
is the child process. Every process (except process 0) has one parent process, but can have many child processes.

The operating system kernel identifies each process by its process identifier. Process 0 is a special process that
is created when the system boots; after forking a child process (process 1), process 0 becomes the swapper process
(sometimes also known as the "idle task"). Process 1, known as init, is the ancestor of every other
process in the system.
'''

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'): # only available on Unix
        print 'parent process:', os.getppid()
    time.sleep(30)
    print 'process id:', os.getpid()

def f(name):
    info('\033[31;1mfunction f\033[0m')
    print 'Hello', name

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    print '--------------'
    p = Process(target=f, args=('chris',))
    p.start()
    p.join()