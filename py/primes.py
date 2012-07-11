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
            i = _add_prime(primes, i)
            yield i

    @staticmethod
    def primes_less_than(n):
        '''
        Generates all primes less than n
        '''

        if n < 2:
            raise StopIteration
        else:
            yield 2
        
        primes = [2]
        i = 3
        while True:
            i = PrimeGenerators._add_prime(primes, i)
            if i > n:
                raise StopIteration

            yield i
            i += 1

    @staticmethod
    def _add_prime(primes, i):
        while True:
            isprime = True
            for d in primes[0:int(math.sqrt(primes[-1]))]:
                if i % d == 0:
                    isprime = False
                    break

            if isprime:
                primes.append(i)
                #if len(primes) % 1000 == 0:
                    #print(i)
                return i

            i += 1


    

