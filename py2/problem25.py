#!/usr/local/bin/python

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def problem25(n):
    n_1 = 1
    n_2 = 0
    i = 1
    while len(str(n_1)) < n:
        temp = n_1
        n_1 += n_2
        n_2 = temp
        i += 1

    #print(n_1)
    return i


def main():
    #print("Hello World!")
    print(problem25(1000))


main()



