"""
http://projecteuler.net/problem=3 

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""
import math

def isprime(bignum):

    primeTest = 0
    testNum = int (math.sqrt(bignum))

    while (testNum > 1):
        testFact = int (bignum / testNum)
        testInt = testFact * testNum
        if (testInt == bignum):
            return 0
        testNum -= 1

    return 1
    
def isprimefactor(biggernum, biggestnum):
    
    if (isfactor(biggernum, biggestnum)):
        if (isprime(biggernum)):
            return 1
        return 0
    return 0

def isfactor(biggernum, biggestnum):
#   print 'isfactor ...'
#   print '    biggestnum = ', biggestnum, ' biggernum = ', biggernum 
    
    compfactor = int (biggestnum / biggernum)
#   print 'return value = ', ( (compfactor * biggernum) == biggestnum)        
    return ( (compfactor * biggernum) == biggestnum)        

biggestnum = 600851475143

biggernum = int (math.sqrt (biggestnum)) + 1
gotprimefactor = 0

while (gotprimefactor == 0):
    biggernum -= 1
    if isprimefactor(biggernum, biggestnum):
        gotprimefactor = 1

print biggernum, ' is a prime factor of ', biggestnum
