# -*- coding:utf-8 -*-
__auth__ = 'christian'

class A(object):
    def save(self):
        print "save A."

class B(A):
    pass

class C(A):
    def save(self):
        print "save C."

class D(B, C):
    pass

class E(C, B):
    pass

test = D()
test.save()

test1 = E()
test1.save()