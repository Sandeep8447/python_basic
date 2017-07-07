# -*- coding:utf-8 -*-
__auth__ = 'christian'


def is_prime(x):
    if x < 2:
        return False
    prime_flag = True
    for i in range(2,x):
        if x % i == 0:
            prime_flag = False
            break
    return prime_flag


def get_primes(input_list):
    return (element for element in input_list if is_prime(element))


if __name__ == '__main__':
    lst = [9, 8, 24, 56, 7, 3, 189, 156, 155, 131, 23]
    l = get_primes(lst)
    for j in l:
        print j
    print is_prime(1005)