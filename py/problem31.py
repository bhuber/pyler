#!/usr/local/bin/python

"""
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1L1 + 150p + 220p + 15p + 12p + 31p
How many different ways can L2 be made using any number of coins?
"""

from collections import Counter

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()

#
#class MyCounter(Counter):
#    def __hash__(self):
#        result = 0
#        for (k, v) in self.items():
#            result ^= k.__hash__()
#            result *= v
#        return int(result)
#
#
#def problem31(n, current=MyCounter(), cs=0, known=set(), tested=set()):
#    #import ipdb; ipdb.set_trace()
#    if n < 1:
#        return 0
#    if n == 1:
#        return 1
#    #if n in tested:
#        #return known
#
#    #tested.add(n)
#    for c in coins:
#        if cs + c > n:
#            continue
#        else:
#            temp = current.copy()
#            temp[c] += 1
#            if cs + c == n:
#                known.add(temp)
#            else:
#                problem31(n, temp, cs + c, known, tested)
#
#    return known
#


def problem31_enum(n, vals=coins):
    if n < 0 or len(vals) < 1:
        import ipdb; ipdb.set_trace()
        raise Exception("Illegal state encountered in problem31")
    elif len(vals) == 1:
        c = vals[0]
        if c < n:
            return problem31(n - c, vals)
        elif c == n:
            return c
        else:
            import ipdb; ipdb.set_trace()
            raise Exception("Illegal state encountered in problem31")
    else:
        result = []
        for i in xrange(0, len(vals)):
            c = vals[i]
            if c > n:
                continue
            elif c == n:
                result.append(c)
            else:
                tail = problem31(n - c, vals[i:])
                result.append((c, tail))

        return result


def problem31(n, vals=coins):
    if n < 0 or len(vals) < 1:
        raise Exception("Illegal state encountered in problem31")
    elif len(vals) == 1:
        c = vals[0]
        if c < n:
            return problem31(n - c, vals)
        elif c == n:
            return 1
        else:
            raise Exception("Illegal state encountered in problem31")
    else:
        result = 0
        for i in xrange(0, len(vals)):
            c = vals[i]
            if c > n:
                continue
            elif c == n:
                result += 1
            else:
                result += problem31(n - c, vals[i:])

        return result


def main():
    print(problem31(200))


main()



