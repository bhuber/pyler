#!/usr/local/bin/python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def problem4(digits = 2):
    pmax = 0
    start = 10 ** digits
    end = 10 ** (digits - 1)
    for i in xrange(start, end, -1):
        for j in xrange(start, end, -1):
            #early abort if we've definitely found the max
            if i == j and i * i < pmax:
                return pmax

            p = i * j
            strp = str(p)
            if p < pmax:
                continue
            elif strp == strp[::-1]:
                pmax = p

    return pmax


def main():
    #print("Hello World!")
    print(problem4(3))


main()



