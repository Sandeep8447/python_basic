# -*- coding:utf-8 -*-
__auth__ = 'christian'

import random
print random.random()
print random.randint(1,2)
print random.randrange(1,10)

checkcode = ''
for i in range(6):
    current = random.randrange(0,6)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print checkcode


code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
print code
print ''.join(code)

'''
+=，每次都需要开辟内存空间运算
join的效率高，只需要一次就好
'''