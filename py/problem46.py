#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as
the sum of a prime and twice a square?
"""

from primes import PrimeGenerators

_pg = PrimeGenerators()

# Odd composite numbers
_ocs = [9, 15]

# Tuple, first element is set of squares lower than x^2, second element is x
_squares = ({i*i for i in xrange(1, 100)}, 101)


def next_oc():
    """Gets the next odd composite number, adds missing ones to _ocs"""
    candidate = _ocs[-1] + 2
    while _pg.isprime(candidate):
        candidate += 2
    _ocs.append(candidate)
    return candidate


def ocs():
    """Generates odd composite numbers forever"""
    for oc in _ocs:
        yield oc

    while True:
        oc = next_oc()
        yield oc


def is_twice_sq(i):
    """Returns true if i is of the form 2*(x**2), false otherwise"""
    if (i & 1) == 1:
        return False
    ps = i / 2
    max_sq = _squares[1]**2
    if ps > max_sq:
        # Add squares until we have enough
        x = _squares[1]
        x2 = x*x
        squares = _squares[0]
        while x2 < ps:
            squares.add(x2)
            x += 1
            x2 = x*x
        _squares[1] = x

    return ps in _squares[0]

#### Main program ####


def main():
    for oc in ocs():
        if oc % 9999 == 0:
            print("Testing oc %i" % oc)
        found = False
        for p in _pg.primes_less_than(oc):
            if is_twice_sq(oc - p):
                found = True
                break
        if not found:
            print("Found first odd composite: %i" % oc)
            return


main()
