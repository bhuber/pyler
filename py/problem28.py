#!/usr/local/bin/python

"""
Problem 28
11 October 2002

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def problem28(n):
    """
    let f(n) = sum of corners of an nxn spiral (note n is always odd)
    let n_1 = n - 1
    let n_2 = n - 2
    f(1) = 1
    f(n) = ((n_2)^2 + 1*n_1) + ((n_2)^2 + 2*n_1) + ((n_2)^2 + 3*n_1) + ((n_2)^2 + 4*n_1)
         = 4 * (n_2)^2 + 10 * n_1

    check: 
        13 + 17 + 21 + 25 = 76
        4 * (3 * 3) + 10 * 4 = 76

    let g(n) = sum of diagonals of an nxn spiral
             = f(n) + f(n - 2) + ... + f(1)
             = f(1) + f(3) + ... + f(n)
             = 1 + (4 * 1^2 + 10 * 2) + (4 * 3^2 + 10 * 4) + ... + 
                 (4 * k_i^2 + 10 + k_(i + 1)) + ... + (4 * n_2^2 + 10 * n_1)
             = 1 + sum(4 * (2i + 1)^2 + 10 * (2(i + 1)), i, i = 1, i < floor(n/2))
             = 1 + 4 * sum((odd numbers less than n) squared) + 10 * sum(even numbers less than n)

    let s(n)    = sum of i <= n
                = n * (n + 1) / 2

    let ss(n)   = sum of squares <= n
                = n * (n + 1) * (2 * n + 1) / 6

    let ses(n)  = sum of even squares <= n 
                = sum((2*i)^2, i = 1, i <= n/2) 
                = 4 * sum(i^2, i = 1, i <= n/2) 
                = 4 * ss(n / 2)

    let sos(n)  = sum of odd squares <= n
                = ss(n) - ses(n)

    let e(n)    = sum of even i <= n 
                = 2 * s(n / 2)

    g(n) = 1 + 4 * sos(n - 1) + 10 * e(n - 1)
    """
    return g(n)

def s(n): return n * (n + 1) / 2
def ss(n): return n * (n + 1) * (2 * n + 1) / 6
def ses(n): return 4 * ss(n / 2)
def sos(n): return ss(n) - ses(n)
def e(n): return 2 * s(n / 2)
def g(n): return 1 + 4 * sos(n - 1) + 10 * e(n - 1)

def main():
    #print("Hello World!")
    print(problem28(1001))


main()

