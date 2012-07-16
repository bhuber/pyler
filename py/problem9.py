#!/usr/local/bin/python

"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def problem9(n):
    result = []
    for a in xrange(1, n):
        for b in xrange(a, n):
            c = math.sqrt(a * a + b * b)
            if c == int(c) and a + b + c == n:
                result.append((a, b, int(c)))

    return result



def main():
    #print("Hello World!")
    results = problem9(1000)
    print(results)
    print(list(map(lambda t: reduce(lambda a, b: a * b, t), results)))


main()



