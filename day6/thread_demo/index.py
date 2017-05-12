# -*- coding:utf-8 -*-
__auth__ = 'christian'

from threading import Thread
import time
def Foo(arg):
    for item in range(30):
        print item
        time.sleep(1)


print 'before'
t1 = Thread(target=Foo, args=('dddd',)) # threading combine with function
#t1.setDaemon(True)  # before start threading
t1.start()
t1.join(timeout=1)

print t1.getName()

print 'after'
print 'after'
print 'after'
print 'after end'
#time.sleep(10)
# master thread destroy
