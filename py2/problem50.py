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
from bisect import bisect_left

_pg = PrimeGenerators()


def find_prime_with_longest_sum(n):
    primes = list(_pg.primes_less_than(n))
    prime_sums = [[p, []] for p in primes]
    length = len(primes)
    for hi in xrange(1, length):
        if hi % 5000 == 0:
            print('Window max at %i' % hi)

        p_hi = primes[hi]
        if p_hi > n / 2:
            break
        window = deque([primes[hi]])
        window_sum = primes[hi]
        for low in xrange(hi - 1, -1, -1):
            # work backwards so that when window_sum gets too big we can abort
            np = primes[low]
            window_sum += np
            window.appendleft(np)
            if window_sum > n:
                break

            # Binary search primes list to see if window_sum is prime (saves us a hashtable)
            idx = bisect_left(primes, window_sum)
            if idx != len(primes) and primes[idx] == window_sum:
                entry = prime_sums[idx]
                if len(entry[1]) < len(window):
                    entry[1] = list(window)

    # Return (prime, sum_list) pair with longest sum_list
    return max(prime_sums, key=lambda ps: len(ps[1]))


def print_results(n):
    result = find_prime_with_longest_sum(n)
    sum_str = ' + '.join(map(str, result[1]))
    print('Longest prime sum less than %i: %i = %s' % (n, result[0], sum_str))


print_results(100)
print_results(1000)
print_results(1000000)
