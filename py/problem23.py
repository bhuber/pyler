#!/usr/local/bin/python

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from primes import PrimeMethods
import itertools

def is_abundant(n):
    if n < 12:
        return False

    spd = PrimeMethods.sopdf(n, 1) - n
    return spd > n
    
a_limit = 28123

def problem23():
    abundants = []
    for i in xrange(1, a_limit + 1):
        if is_abundant(i):
            abundants.append(i)

    sum_of_abundants = set()
    length = len(abundants)
    for i in xrange(length):
        for j in xrange(length):
            a_1 = abundants[i]
            a_2 = abundants[j]
            aa = a_1 + a_2
            if aa > a_limit:
                break
            sum_of_abundants.add(aa)

    u = set(range(1, a_limit + 1))
    not_sum = u - sum_of_abundants
    #print(sorted(not_sum))
    return sum(not_sum)

def problem23_v2():
    abundants = []
    for i in xrange(1, a_limit + 1):
        if is_abundant(i):
            abundants.append(i)

    sum_of_abundants = set()
    not_sum = set(range(1, a_limit + 1))
    length = len(abundants)
    for i in xrange(length):
        for j in xrange(i, length):
            a_1 = abundants[i]
            a_2 = abundants[j]
            aa = a_1 + a_2
            if aa in not_sum:
                not_sum.remove(aa)

    #print(sorted(not_sum))
    return sum(not_sum)

def main():
    #print("Hello World!")
    print(problem23_v2())


main()



