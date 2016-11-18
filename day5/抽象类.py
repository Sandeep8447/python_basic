# -*- coding:utf-8 -*-
__auth__ = 'christian'

from abc import ABCMeta, abstractmethod
class Bar(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Fun(self):
        pass

class Foo(Bar):
    def __init__(self):
        print "__init__"

Foo()