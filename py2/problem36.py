#!/usr/local/bin/python

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def problem36(n):
    result = []
    for i in xrange(0, n):
        if palindrome(i, 2) and palindrome(i, 10):
            result.append(i)
    return result


def combine_digits(digits, base=10):
    def dti(a):
        if isinstance(a, int) or isinstance(a, long):
            return a
        else:
            return int(a) if '0' <= ord(a) <= '9' else ord(a.upper()) - ord('A') + 10

    return reduce(lambda a, b: base * dti(a) + dti(b), digits)

def palindrome(n, radix=10):
    s = itoa(n, radix)
    length = len(s)
    for i in xrange(0, length):
        a = s[i]
        b = s[length - 1 - i]
        if a != b:
            return False
    return True


def itoa(i, base=10):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
              "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
              "X", "Y", "Z"]
    result = ''
    i = long(i)
    if base == 10:
        return str(i)
    if i == 0:
        return '0'
    sign = ''
    if i < 0:
        i *= -1
        sign = '-'

    quotient = i
    while quotient != 0:
        remainder = quotient % base
        quotient = quotient / base
        result = digits[remainder] + result
        
    return sign + result

    


def main():
    ans = problem36(10 ** 6)
    print(sum(ans))


main()




