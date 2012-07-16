#!/usr/local/bin/python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from primes import PrimeGenerators

def problem10(n):
    return sum(PrimeGenerators.primes_less_than(n))


def main():
    #print("Hello World!")
    print(problem10(2000000))


main()



