#!/usr/local/bin/python

"""
http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum(start, end, divisors=[3, 5]):
    result = 0
    for i in xrange(start, end):
        for d in divisors:
            if i % d == 0:
                result += i
                break

    return result


def main():
    #print("Hello World!")
    print(sum(1, 1000))

main()



