#!/usr/local/bin/python

"""
This is meant to be a module for dealing with primes
"""

import math

class PrimeGenerators(object):
    '''
    Class for defining generators for prime numbers
    '''

    @staticmethod
    def first_n_primes(n):
        '''
        Generates the first n prime numbers
        '''

        if n < 1:
            raise StopIteration
        else:
            yield 2

        primes = [2]
        i = 3
        while len(primes) < n:
            isprime = True
            for d in primes[0:int(math.sqrt(primes[-1]))]:
                if i % d == 0:
                    isprime = False
                    break

            if isprime:
                primes.append(i)
                yield i

            i += 1


    

