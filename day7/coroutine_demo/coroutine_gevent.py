# -*- coding:utf-8 -*-
__auth__ = 'christian'

import gevent

"""
协程一个标准定义，即符合什么条件就能称之为协程：
必须在只有一个单线程里实现并发
修改共享数据不需加锁
用户程序里自己保存多个控制流的上下文栈
一个协程遇到IO操作自动切换到其它协程

Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
"""


def func1():
    print('\033[31;1mHello 1...\033[0m')
    gevent.sleep(3)
    print('\033[31;1mHello 6...\033[0m')


def func2():
    print('\033[32;1mHello 2...\033[0m')
    gevent.sleep(2)
    print('\033[32;1mHello 5...\033[0m')


def func3():
    print('\033[33;1mHello 3...\033[0m')
    gevent.sleep(1)
    print('\033[33;1mHello 4...\033[0m')

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])