#!/usr/local/bin/python

"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


class CollatzGenerator(object):
    _distance = None

    def __init__(self):
        self._distance = { 1: 0, 2: 1, 4: 2 }

    def __getitem__(self, i):
        if self._distance.has_key(i):
            return self._distance[i]
        else:
            j = i / 2 if (i & 1) == 0 else 3 * i + 1 
            val = self[j] + 1
            self._distance[i] = val
            return val

def problem14(n):
    dist_max = 0
    result = 1
    cg = CollatzGenerator()

    for i in xrange(1, n):
        dist = cg[i]
        if dist > dist_max:
            dist_max = dist
            result = i

    return (result, dist_max)


def main():
    #print("Hello World!")
    print(problem14(1000000))


main()



