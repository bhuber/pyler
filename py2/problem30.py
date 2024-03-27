#!/usr/local/bin/python

"""
08 November 2002

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def problem30(n):
    result = powers(n)
    print(result)
    return sum(result)

def digits(n):
    return [int(i) for i in str(n)]

def powers(n):
    i = 2
    result = []
    n_digits = [2]
    while i <= (9 ** n * len(n_digits)):
        n_digits = digits(i)
        if i == sum([j ** n for j in n_digits]):
            result.append(i)

        i += 1

    return result


def main():
    #print("Hello World!")
    print(problem30(5))


main()



