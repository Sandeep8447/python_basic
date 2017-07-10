# -*- coding:utf-8 -*-
__auth__ = 'christian'


from greenlet import greenlet

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

