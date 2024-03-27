#!/usr/local/bin/python

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools

def fact(n):
    return 1 if n < 2 else n * fact(n - 1)

def problem24(k, n):
    perm = range(k)
    count = 0
    for i in itertools.permutations(perm):
        count += 1
        if count == n:
            return "".join([str(s) for s in i])

    return None

def problem24_v2(k, n):
    return "".join([str(s) for s in permute(range(k), n)])

def permute(opts, n):
    """
    opts is a list of items to permute, assumed to be sorted
    n is the nth permutation to get
    """
    if len(opts) == 1:
        return [opts[0]]

    if n == 0:
        return opts
        
    total = fact(len(opts) - 1)
    i = 0
    while n > total:
        n -= total
        i += 1

    first = opts[i]
    del opts[i]
    return [first] + permute(opts, n)
     



def main():
    #print("Hello World!")
    print(problem24_v2(10, 1000000))



main()



