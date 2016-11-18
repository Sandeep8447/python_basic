# -*- coding:utf-8 -*-
__auth__ = 'christian'

class People(object):
    info = 'mark'  # public arg or class arg 类变量，实例化后的所有实例共有属性，实例化后，都一样，是独立的，实例化后会生成新的变量，改动后只会对该实例生效。
    info_dic = {   #实例共享，name的value变了，所有的实例的value都变了
        'name' : 't',
        'age'  : '21'
    }
    def __init__(self, name, age, job, gender):  # init func, generate init data, 初始化函数，也叫构造函数，初始化实例的时候会自动执行。
        self.Name = name  # 公有变量，实例化后的实例的变量。
        self.Aag = age
        self.Job = job
        self.info = 'mark it'
        self.__Gender = gender # 私有变量，私有属性，静态的，只读不能改
        print name, age, job


    def __breath(self):   # 私有方法，只能在类的内部调用
        print "%s is breathing..." % self.Name

    def get_info(self, info_type):
        if info_type == 'gender':
            return self.__Gender

    def walk(self):  # 公有方法
        print "I'm working.....",self.Job
        self.__breath()

    def talk(self):
        print "I'm talking with sb....", self.Name


p1 = People("hanmeimei", 29, "beautiful girl",'F')

p1.walk()
p1.talk()
print p1.info
print People.info

print '***'
print p1.get_info('gender')



#People.talk(p1)  # self = p1
p2 = People("LiLei", 29, "handsome boy", 'M')
p2.walk()
p2.talk()
print p2.info
print People.info


p3 = People("DAVID", 21, "handsome boy", 'M')
p3.walk()
p3.talk()
#注意这个的不同
print p3.info
print People.info


print "---------------------"
p1.info = 'P1'
print "p1:", p1.info
print "p2", p2.info
print "p3", p3.info

p1.info_dic['name'] = "hello world"

print p1.info_dic['name']
print p2.info_dic['name']
print p3.info_dic['name']