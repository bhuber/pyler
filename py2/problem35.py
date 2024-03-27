#!/usr/local/bin/python

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from primes import PrimeGenerators


def problem35(n):
    cps = set()
    first_n_primes = set()
    for p in PrimeGenerators.primes_less_than(n):
        first_n_primes.add(p)

    def check_circular(p):
        if p in cps:
            return
        sp = str(p)
        length = len(sp)
        digits = [int(i) for i in sp]
        cycles = []
        for i in xrange(0, length):
            t = combine_digits(digits)
            if not t in first_n_primes:
                return
            cycles.append(t) 
            digits = rotate_left(digits)

        cps.update(cycles)

    for p in first_n_primes:
        check_circular(p)

    return cps 


def rotate_left(l):
    if l is None or len(l) < 2:
        return l
    result = l[1:]
    result.append(l[0])
    return result


def combine_digits(digits):
    return reduce(lambda a, b: 10 * a + b, digits)


def main():
    cps = problem35(10 ** 6)
    print(sorted(cps))
    print(len(cps))


main()



