#!/usr/local/bin/python

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

import csv

filename = "names.txt"

def string_score(s):
    base = ord('A')
    score = 0
    for c in s.upper():
        score += ord(c) - base + 1

    return score


def problem22(filename):
    reader = csv.reader(open(filename, 'rb'))
    names = reader.next()
    names.sort()
    scores = [(i + 1) * string_score(names[i]) for i in xrange(0, len(names))]
    return sum(scores)


def main():
    #print("Hello World!")
    print(problem22(filename))


main()



