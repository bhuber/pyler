#!/usr/local/bin/python

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

number_to_word = {
    -1:     "negative",
    0:      "zero",
    1:      "one",
    2:      "two",
    3:      "three",
    4:      "four",
    5:      "five",
    6:      "six",
    7:      "seven",
    8:      "eight",
    9:      "nine",
    10:     "ten",
    11:     "eleven",
    12:     "twelve",
    13:     "thirteen",
    14:     "fourteen",
    15:     "fifteen",
    16:     "sixteen",
    17:     "seventeen",
    18:     "eighteen",
    19:     "nineteen",
    20:     "twenty",
    30:     "thirty",
    40:     "forty",
    50:     "fifty",
    60:     "sixty",
    70:     "seventy",
    80:     "eighty",
    90:     "ninety",
    100:    "hundred",
    1000:   "thousand",

    10 ** 6:    "million",
    10 ** 9:    "billion",
    10 ** 12:   "trillion",
    10 ** 15:   "quadrillion",
    10 ** 18:   "quintillion",
    10 ** 21:   "sextillion",
    10 ** 24:   "septillion",
    10 ** 27:   "octillion",
    10 ** 30:   "nonillion",
    10 ** 33:   "decillion"
}

def pretty_int(i):
    i = int(i)
    nw = number_to_word
    max_i = max(nw.keys()) * 1000
    over = "bunches and bunches"
    result = ""

    if i < 0:
        return nw[-1] + " " + pretty_int(-1 * i)
    elif i <= 20:
        return nw[i]
    elif i < 100:
        result = nw[(i / 10) * 10] 
        remainder = i % 10
        if remainder != 0:
            result += "-" + pretty_int(i % 10)

        return result
    elif i < 1000:
        result = nw[i / 100] + " " + nw[100]
        remainder = i % 100
        if remainder != 0:
            result += " and " + pretty_int(remainder)

        return result
    elif i < max_i:
        n_digits = len(str(i))
        highest_key = 10 ** (((n_digits - 1) / 3) * 3)
        top = i / highest_key
        if top != 0:
            result = pretty_int(top) + " "
            
        result += nw[highest_key]
        remainder = i % highest_key

        if remainder > 0 and remainder < 100:
            result += " and " + pretty_int(remainder)
        elif remainder >= 100:
            result += ", " + pretty_int(remainder)

        return result
    else:
        return over

def problem17(n):
    return sum([len(filter(lambda c: c not in set(",- "), pretty_int(i))) for i in xrange(1, n)])


def main():
    #print("Hello World!")
    print(problem17(1001))


main()



