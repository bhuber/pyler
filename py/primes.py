#!/usr/local/bin/python

"""
This is meant to be a module for dealing with primes
"""

import math
import pdb

class PrimeGenerators(object):
    '''
    Class for defining generators for prime numbers
    '''

    _primes = None

    def __init__(self):
        self._primes = [2]
    
    def __getitem__(self, nth_prime):
        if nth_prime < len(self._primes):
            return self._primes[nth_prime]

        
        #pdb.set_trace()
        i = self._primes[-1] + 1
        while nth_prime >= len(self._primes):
            i = PrimeGenerators._add_prime(self._primes, i)
            i += 1

        return self._primes[nth_prime]


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
            i = PrimeGenerators._add_prime(primes, i)
            yield i
            i += 1

    @staticmethod
    def all_primes():
        '''
        Generates prime numbers indefinitely
        '''

        primes = [2]
        i = 3
        while True:
            i = PrimeGenerators._add_prime(primes, i)
            yield i
            i += 1

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


class PrimeMethods(object):
    '''
    Defines some common functions involving prime numbers
    '''

    @staticmethod
    def n_factors(divisors):
        '''
        divisors is a dictionary, where key is a prime factor and value is its exponent
        for example, the dictionary for 18 would be { 2: 1, 3: 2 }
        '''

        #see http://en.wikipedia.org/wiki/Divisor_function
        keys_plus_1 = map(lambda a: a + 1, divisors.values())
        if len(keys_plus_1) > 1:
            return reduce(lambda a, b: a * b, keys_plus_1)
        else:
            return len(keys_plus_1)

    @staticmethod
    def get_prime_factors(n):
        '''
        Given n, find its prime factors
        returns a dictionary where keys are primes, values are exponents
        '''

        sqrt_n = math.sqrt(n)
        prime_max = sqrt_n

        i = 0
        p = 2
        result = { }
        while p < prime_max and p < sqrt_n and n > 1:
            p = PrimeMethods._prime_gen[i]
            i += 1
            keep_trying = True

            while keep_trying:
                if n % p == 0:
                    n /= p
                    sqrt_n = math.sqrt(n)
                    if not result.has_key(p):
                        result[p] = 1
                    else:
                        result[p] += 1
                else:
                    keep_trying = False

        #last value of n was a prime, so add it
        if n != 1:
            result[n] = 1

        return result



    _prime_gen = PrimeGenerators()



    

