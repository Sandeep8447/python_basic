# -*- coding:utf-8 -*-
__auth__ = 'christian'

# why we need Generator ？

# Just remember that a generator is a special type of iterator.

'''
1. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the
yield key word rather than return. If the body of a def contains yield, the function automatically becomes a generator 
function(even if it also contains a return statement). There's nothing else we need to do to create one.

2. Just remember that a generator is a special type of iterator.

3. To be considered an iterator, generators must define a few methods, one of which is__next__(). To get the next value 
from a generator, we use the same built-in function as for iterators:next().

4. python 2.7.x next(), python 3.5.x __next__()

5. Again, this bears repeating: yield is just return(plus a little magic) for generator functions.
'''


def simple_generator_function():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    my_generator = simple_generator_function()
    for value in my_generator:
        print(value)
    print next(my_generator)

    # my_generator = simple_generator_function()
    # print my_generator.next()
    # print my_generator.next()
    # print my_generator.next()
    # print my_generator.next()

    # print next(my_generator)
    # print next(my_generator)
    # print next(my_generator)
    # print next(my_generator)


'''
If a generator function calls return or reaches the end its definition, a StopIteration exception is raised. This signals 
to whoever was calling next() that the generator is exhausted (this is normal iterator behavior). It is also the reason 
the while True:loop is present in get_primes. If it weren't, the first time next() was called we would check if the 
number is prime and possibly yield it. If next() were called again, we would uselessly add 1 to number and hit the end 
of the generator function(causing StopIteration to be raised). Once a generator has been exhausted, calling next() on 
it will result in an error, so you can only consume all the values of a generator once. The following will not work:

Traceback (most recent call last):
  File "/home/duanlian/PycharmProjects/python_basic/day7/coroutine_demo/why_generator.py", line 34, in <module>
    print next(my_generator)
StopIteration
'''
