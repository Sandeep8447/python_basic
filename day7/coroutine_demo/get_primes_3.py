# -*- coding:utf-8 -*-
__auth__ = 'christian'

# why we need Generator ？

# Just remember that a generator is a special type of iterator.


def is_prime(x):
    if x < 2:
        return False
    prime_flag = True
    for i in range(2, x):
        if x % i == 0:
            prime_flag = False
            break
    return prime_flag


# the first function without yield key word.
# def get_primes(start):
#     for element in range(start):
#         if is_prime(element):
#             return element


'''
Clearly, in get_primes, we would immediately hit the case where number = 3 and return at line 4. Instead of return, 
we need a way to generate a value and, when asked for the next one, pick up where we left off.
Functions, though, can't do this. When they return, they're done for good. Even if we could guarantee a function would be
called again, we have no way of saying, "OK, now, instead of starting at the first line like we normally do, start up 
where we left off at line 4." Functions have a single entry point: the first line.
'''


# rewrite the get_primes as a generator function.
# the second function we use Generator with the yield key word.
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
# Remember, yield both passes a value to whoever called next(), and saves the "state" of the generator function.
        number += 1
'''
The while loop is there to make sure we never reach the end of get_primes. It allows us to generate a value for as long 
as next()is called on the generator. This is a common idiom when dealing with infinite series (and generators in general).
'''

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    # Find the sum of all the primes below two million.
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 20000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == '__main__':
    solve_number_10()