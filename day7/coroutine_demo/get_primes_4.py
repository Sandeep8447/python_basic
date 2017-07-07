# -*- coding:utf-8 -*-
__auth__ = 'christian'

import math
# why we need Generator ？

# Just remember that a generator is a special type of iterator.


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


'''
The next line of get_primes takes a bit of explanation. While yield number would yield the value of number, a statement 
of the form 'other = yield foo' means, "yield foo and, when a value is sent to me, set other to that value."
You can "send" values to a generator using the generator's send method.
'''


def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1


'''
To illustrate how values are sent to a generator, let's return to our prime number example. This time, instead of simply
printing every prime number greater than number, we'll find the smallest prime number greater than successive powers of 
a number (i.e. for 10, we want the smallest prime greater than 10, then 100, then 1000, etc.). We start in the same way 
as get_primes:
'''
# successive powers of a number: 一个数的连续的幂级数


def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

'''
Two things to note here: First, we're printing the result of generator.send, which is possible because send both sends 
a value to the generator and returns the value yielded by the generator (mirroring how yield works from within the 
generator function).

Second, notice the prime_generator.send(None) line. When you're using send to "start" a generator (that is, execute the 
code from the first line of the generator function up to the first yield statement), you must sendNone. This makes sense, 
since by definition the generator hasn't gotten to the first yield statement yet, so if we sent a real value there would
be nothing to "receive" it. Once the generator is started, we can send values as we do above.
'''

if __name__ == '__main__':
    print_successive_primes(10, base=10)