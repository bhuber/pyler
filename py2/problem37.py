#!/usr/local/bin/python

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from primes import PrimeGenerators

p = PrimeGenerators()

def problem37():
    result = []
    i = 0
    while len(result) < 11:
        prime = p[i]
        if truncatable(prime):
            result.append(prime)
        i += 1

    return result


def truncatable(n1):
    def _truncatable(n2, lr):
        if not p.isprime(n2):
            return False

        s = str(n2)
        if len(s) == 1:
            return True
        else:
            l = s[0:-1]
            r = s[1:]
            trunc = s[0:-1] if lr == "l" else s[1:]
            return _truncatable(int(trunc), lr)

    return n1 > 10 and _truncatable(n1, "l") and _truncatable(n1, "r")

def main():
    print(sum(problem37()))


main()

