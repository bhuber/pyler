#!/usr/local/bin/python

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations


def problem32():
    results = set()
    pandigitals = []
    firsts = range(1, 5)
    #[1 2 3 4 5 6 7 8 9]
    for p in permutations(xrange(1, 10)):
        for first in firsts:
            m1 = combine_digits(p[:first])
            if m1 == 2 or m1 == 5:
                continue
            for second in xrange(first + 1, 6):
                #After 5 digits are eaten up by m1, and m2, we can't possibly have a solution
                m2 = combine_digits(p[first:second])
                prod = combine_digits(p[second:])
                if m1 * m2 == prod:
                    results.add(prod)
                    pandigitals.append((m1, m2, prod))
                    print((m1, m2, prod))

    return (results, pandigitals)


def combine_digits(digits):
    return reduce(lambda a, b: 10 * a + b, digits)


def main():
    r_pd = problem32()
    #print(r_pd[1])
    print(sum(r_pd[0]))


main()



