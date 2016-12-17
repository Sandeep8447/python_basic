# -*- coding:utf-8 -*-
__auth__ = 'christian'

def fib_direct(n):
    assert n > 0, 'invalid n'
    if n < 3:
        return 1
    else:
        return fib_direct(n - 1) + fib_direct(n - 2)

if __name__ == '__main__':
    print fib_direct(40)