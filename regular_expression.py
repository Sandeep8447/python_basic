# -*- coding:utf-8 -*-
__auth__ = 'christian'

import re
import time

bill_date = time.strftime("%Y-%m-%d")
re_date = re.search("\d+\-\d*",bill_date).group()
print re_date


pattern = re.compile(r'hello')
match = pattern.match('hello world!')
if match:
    print match.group()

m1 = pattern.search('hello wrold!')
if m1:
    print m1.group()
    print m1.groups()
print "*********************"

p = re.compile(r'\d+')
print p.split('hello2world3man4')
print p.findall('hello2world3man4')

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print p.subn(r'\2 \1', s)


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print p.subn(func, s)


print "***********************************************"
m = re.match(r'(\w+)(\w+)(?P<sign>.*)', 'hello world!')
#m = re.match(r'(\w+)(?P<name>abc)','abcabcadcabc')
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup

#print m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')
