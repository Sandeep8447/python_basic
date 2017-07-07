# -*- coding:utf-8 -*-
__auth__ = 'christian'

import math


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


def get_primes(input_list):
    return (element for element in input_list if is_prime(element))


if __name__ == '__main__':
    lst = [9, 8, 24, 56, 7, 3, 189, 156, 155, 131, 23]
    l = get_primes(lst)
    for i in l:
        print i
    print is_prime(19)