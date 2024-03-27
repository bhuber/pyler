#!/usr/local/bin/python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import primes

def lcm(ints):
    '''
    Prints the Least Common Multiple of the items in ints
    ints: a list of integers to find the lcm for; must be iterable
    '''

    state = list(ints)
    pmax = max(state)
    divisors = []

    for p in primes.PrimeGenerators.first_n_primes(pmax):
        #if True, we found an element in state for which p was a divisor
        got_divisor = True

        while got_divisor:
            got_divisor = False

            for i in xrange(0, len(state)):
                s = state[i]
                if s % p == 0:
                    state[i] = s / p
                
                    #only one copy per while-loop iteration plz
                    if not got_divisor:
                        divisors.append(p)

                    got_divisor = True

        if all_equal(state):
            break

    #print(state)
    #print(divisors)
    return reduce(lambda a, b: a * b, divisors)

def all_equal(x):
    '''
    Returns True if all the elements of x are equal
    x: some iterable
    '''
    a = x[0]
    for i in x:
        if i != a:
            return False

    return True


def main():
    #print("Hello World!")
    print(lcm(xrange(1, 11)))
    print(lcm(xrange(1, 21)))


main()



