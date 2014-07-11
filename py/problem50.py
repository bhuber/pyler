#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


from primes import PrimeGenerators
from collections import deque

_pg = PrimeGenerators()


def find_longest_prime_sum(n):
    primes = _pg
    low_idx = 0
    high_idx = 1
    window = deque([primes[low_idx], primes[high_idx]])
    psum = sum(window)
    limit = n / 2
    result = []
    while primes[low_idx] < limit and len(window) > 0:
        if psum < n:
            high_idx += 1
            np = primes[high_idx]
            window.append(np)
            psum += np
        elif psum == n:
            if len(result) < len(window):
                result = list(window)
            high_idx += 1
            np = primes[high_idx]
            window.append(np)
            psum += np
        elif psum > n:
            low_idx += 1
            np = window.popleft()
            psum -= np

    return result


def find_prime_with_longest_sum(n):
    prime_sums = [(p, find_longest_prime_sum(p)) for p in _pg.primes_less_than(n)]
    return max(prime_sums, key=lambda ps: len(ps[1]))


def print_results(n):
    result = find_prime_with_longest_sum(n)
    sum_str = ' + '.join(map(str, result[1]))
    print('Longest prime sum less than %i: %i = %s' % (n, result[0], sum_str))


print_results(100)
print_results(1000)
print_results(1000000)
