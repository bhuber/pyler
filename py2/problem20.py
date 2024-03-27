#!/usr/local/bin/python

"""
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from primes import PrimeGenerators

def fact(n):
    return 1 if n < 2 else n * fact(n - 1)

def problem20(n):
    return sum([int(c) for c in str(fact(n))])


def main():
    #print("Hello World!")
    print(problem20(100))


main()



