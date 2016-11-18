from operator import itemgetter, attrgetter

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [Student('john', 'A', 15),Student('jane', 'B', 12),Student('dave', 'B', 10), ]
print sorted(student_objects, key=lambda student: student.age)
print sorted(student_objects, key=attrgetter('age'))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print sorted(student_tuples, key=lambda student:student[0])
print sorted(student_tuples, key=itemgetter(1))


print sorted(student_tuples, key=itemgetter(1,2))
print sorted(student_objects, key=attrgetter('grade', 'age'))


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([36, 5, 12, 9, 21], reversed_cmp)
print sorted(['bob', 'about', 'Zoo', 'Credit'])

print sorted(student_objects, key=attrgetter('age'), reverse=True)
print sorted(student_objects, key=attrgetter('age'), reverse=True)


s = sorted(student_objects,key=attrgetter('age')) # sort on secondary key
print sorted(s,key=attrgetter('grade'), reverse=True)


a = [36, 5, 12, 9, 21]
a.sort()
print a

print sorted([1, 3, 9, 5, 0])
print sorted([1, 3, 9, 5, 0], reverse=True)
dict = {
        3:2,
        4:3,
        6:9,
        'a':'test',
        'e':'fff',
        '*':'$',
}

print dict.items()
print sorted(dict.items(), key=lambda x:x[1])

print sorted("My NAME is christian Duan.".split(), key=str.lower)

import functools
sorted_ignore_case = functools.partial(sorted, key=str.lower)
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

def cmp_ignore_case(s1, s2):
    return cmp(s1.lower(), s2.lower())
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


print sorted([1, 3, 9, 5, 0], lambda x, y: -cmp(x,y))