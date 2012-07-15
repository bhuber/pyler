#!/usr/local/bin/python

"""
Problem 26
13 September 2002

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def problem26(n):
    return max([(i, n_digits(i)) for i in xrange(1, 1001)], key = lambda a: a[1])

def n_digits(n):
    remainder = 1
    result = 1
    digits = set()

    while True:
       if remainder in digits or remainder == 0:
           #print(digits)
           return len(digits) - 1

       digits.add(remainder)
       remainder %= n
       remainder *= 10
    

def main():
    #print("Hello World!")
    print(problem26(997))


main()



