# -*- coding:utf-8 -*-
__auth__ = 'christian'


from greenlet import greenlet
"""
协程一个标准定义，即符合什么条件就能称之为协程：
必须在只有一个单线程里实现并发
修改共享数据不需加锁
用户程序里自己保存多个控制流的上下文栈
一个协程遇到IO操作自动切换到其它协程

greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
"""


def test1():
    print 12
    gr2.switch()
    print 36
    gr2.switch()


def test2():
    print 48
    gr1.switch()
    print 72

if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()

