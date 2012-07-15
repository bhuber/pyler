#!/usr/local/bin/python

"""
Problem 27
27 September 2002

Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2 -79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from primes import PrimeGenerators

def quad(n, a, b):
    return n * n + a * n + b

def problem27(alow, ahigh, bhigh):
    pg = PrimeGenerators()
    prime_set = set()
    prime_max = 0
    i_p = 0
    best = [0, None, None]      #[n, a, b]

    for a in xrange(alow, ahigh):
        i_b = 0
        b = pg[i_b]
        while b < bhigh:
            n = 0
            val = quad(n, a, b)
            while val > prime_max:
                prime_max = pg[i_p]
                prime_set.add(prime_max)
                i_p += 1

            while val in prime_set:
                n += 1
                val = quad(n, a, b)

            if n > best[0]:
                best = [n, a, b]

            b = pg[i_b]
            i_b += 1

    return best


def main():
    #print("Hello World!")
    print(problem27(-1000, 1001, 1001))


main()



