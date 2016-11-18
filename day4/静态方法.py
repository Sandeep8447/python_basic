# -*- coding:utf-8 -*-
__auth__ = 'christian'

class MyClass(object):
    age = 22
    def __init__(self):
        self.name = "alex"
    def sayhi(self):  # 必须实例化才能调用
        print "----sayhi 1"
    @staticmethod  # 静态方法，和实例没有什么关系，不需要实例化即可调用，类的工具包
    def sayhi2():
        print "----sayhi 2"
    @classmethod  # 类方法，不需要实例化就可以调用，不能访问实例的数据
    def sayhi3(self):
        print "----sayhi 3", self.age, #self.name 实例化后的数据不能被访问
    @property
    def sayhi4(self):  #属性方法
        print "----sayhi 4", self.name
        return 'test'


m = MyClass
# m.sayhi3()
# MyClass.sayhi3()

print m.sayhi4  #sayhi4后面没有加()，方法没有被调用，函数变成静态属性，不能被调用。