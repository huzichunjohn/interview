#/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number)+1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

if __name__ == "__main__":
    for prime in get_primes(2):
        if prime > 100:
            break
        print prime
