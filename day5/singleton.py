#_*_coding:utf-8_*_

# def singletone(cls):
#     instances = {}
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return  instances[cls]
#     return wrapper
#
# @singletone
# class myClass(object):
#     a = 1
#     def __init__(self, n):
#         self.n = n
#         print '-->n:', n
#         self.tasks = []
#
# c = myClass(10)
# c.tasks.append("c")
# c2 = myClass(11)
# c2.tasks.append("c2")
# print c.n, c2.n
# print c.tasks


#方法2，实现__new__方法
#并将一个类的实例绑定到类的变量__instance上，
#如果cls.instace为None说明没有实例化过，实例化该类，并返回
#如果cls._instance不为None，直接返回cls._instance
'''
class Singleton(object):
    def __new__(cls, *args, **kw): #
        if not hasattr(cls, '_instance'):
            orgi = super(Singleton, cls)
            cls._instance = orgi.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()
two.a = 5
print one.a, two.a
'''

'''
Singleton
意图：

保证一个类仅有一个实例，并提供一个访问它的全局访问点。

适用性：

当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时。

当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时。

'''

class Singleton(object):
    ''''' A python style singleton '''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls, *args, **kw)
        return cls._instance


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print id(s1), s1
    s2 = SingleSpam('spa')
    print id(s2), s2
    print id(s1), s1

