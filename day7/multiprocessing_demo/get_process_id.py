# -*- coding:utf-8 -*-
__auth__ = 'christian'

from multiprocessing import Process
import os

def info(title):
    print title
    print 'moudle name:', __name__
    print 'parent process:', os.getppid()
    print 'process id:', os.getpid()
    print '\n\n'

def f(name):
    info('\033[31;1mfunction f\033[0m')
    print 'hello', name

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('chris',))
    p.start()
    # p.join()