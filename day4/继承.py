# -*- coding:utf-8 -*-
__auth__ = 'christian'


class SchoolMember(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def tell(self):
        print '''-----info of %s-----
                name: %s
                age: %s
                gender: %s
        ''' % (self.name, self.name, self.age, self.gender)

class School(object):
    def __init__(self, school_name, addr, tel):
        self.school_name = school_name
        self.addr = addr
        self.tel = tel
        self.stu_list = []
        self.tech_list = []


class Student(SchoolMember):
    def __init__(self, name, age, gender, grade, school):
        SchoolMember.__init__(self, name, age, gender)
        #super(Student, self).__init__(name, age, gender) #  新式类的继承写法
        self.grade = grade
        self.school = school
        self.school.stu_list.append(self)  # a instance appends to school list.
    def tell(self):
        SchoolMember.tell(self)
        print '''------from school name: %s
            class: %s
            addr: %s''' % (self.school.school_name, self.grade, self.school.addr)
    def pay_money(self):
        print "----%s is paying the tuition fee----" % self.name
    # def __del__(self):
    #     print "-0-----going to delete my self from student list."
    #     self.school.stu_list.pop(self)
    def transfer(self):
        print "-0-----going to delete my self from student list."
        self.school.stu_list.remove(self)
        self.school = None


class Teacher(SchoolMember):
    def __init__(self, name, age, gender, salary, course, school):
        SchoolMember.__init__(self, name, age, gender)
        self.course = course
        self.salary = salary
        self.school = school
    def teaching(self):
        print "Teacher %s is teaching class of %s" % (self.name, self.course)


school = School("fudan", "guoquanlu", 999)
school2 = School("tongji", "zhenghualu", 110)
s = Student('duanlian', 20, 'M', 'class 1 grade 2', school)
s2 = Student('bob', 20, 'M', 'class 1 grade 2', school)
t1 = Teacher('alex', 20, 'M', 'class 1 grade 2', 20, school)
t2 = Teacher('christian', 20, 'M', 'class 1 grade 2', 'English', school2)


s.tell()
s.pay_money()


print school.stu_list


print '----------',len(school.stu_list)

for i in school.stu_list:
    print i.name, i.school.school_name

s2.transfer()

print '----------',len(school.stu_list)

for i in school.stu_list:
    print i.name, i.school.school_name, i.school.stu_list