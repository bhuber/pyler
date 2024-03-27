#!/usr/local/bin/python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from primes import PrimeGenerators

def problem7(n):
    result = 0
    for p in PrimeGenerators.first_n_primes(n):
        result = p

    return result


def main():
    #print("Hello World!")
    print(problem7(10001))


main()



