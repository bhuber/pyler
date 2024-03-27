#!/usr/local/bin/python

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from primes import PrimeMethods

def problem21(n):
    result = 0
    for a in xrange(2, n + 1):
        b = PrimeMethods.sopdf(a, 1) - a
        a_prime = PrimeMethods.sopdf(b, 1) - b
        if a == a_prime and a != b:
            #print((a, b))
            result += a

    return result


def main():
    #print("Hello World!")
    print(problem21(10000))


main()



