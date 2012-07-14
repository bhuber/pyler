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
        if (i & 1) == 0:
            i += 1

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

            i += 2


class PrimeMethods(object):
    '''
    Defines some common functions involving prime numbers
    '''

    @staticmethod
    def n_divisors(n):
        return PrimeMethods.sopdf(PrimeMethods.get_prime_factors(n))

    @staticmethod
    def sopdf(n, k=0):
        """
        Sum of Prime Divisors function
        if d_1, d_2, ..., d_n represent the divisors of n, 
        returns sum(d_i ** k)
        uses formula for sigma_k on http://en.wikipedia.org/wiki/Divisor_function
        """
        factors = PrimeMethods.get_prime_factors(n)
        result = 1
        for p in factors.keys():
            sum_of_exp = 1
            current = 1
            p_k = p ** k
            for i in xrange(1, factors[p] + 1):
                current *= p_k
                sum_of_exp += current

            result *= sum_of_exp

        return result
            

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



    

