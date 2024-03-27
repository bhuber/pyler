#!/usr/local/bin/python

"""
The sum of the squares of the first ten natural numbers is,

1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10) ** 2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def problem6(n):
   sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
   square_of_sum = n * n * (n + 1) * (n + 1) / (2 * 2) 
   return square_of_sum - sum_of_squares


def main():
    #print("Hello World!")
    print(problem6(100))


main()



