# -*- coding:utf-8 -*-
__auth__ = 'christian'

import time


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        # Remember, yield both passes a value to whoever called next(), and saves the "state" of the generator function.
        print("[%s] is eating baozi %s" % (name, new_baozi))
        time.sleep(1)


def producer():
    # r = con.next()
    r = con.send(None)
    # r = con2.next()
    r = con2.send(None)
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()