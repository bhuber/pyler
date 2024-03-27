#!/usr/local/bin/python

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import datetime, timedelta

def problem19(dom, dow):
    start = datetime(1901, 1, 1)
    end = datetime(2001, 1, 1)
    delta = timedelta(1)
    count = 0

    while start < end:
        if start.day == dom and start.weekday() == dow:
            #print((str(start), start.weekday()))
            count += 1

        start += delta

    return count

def problem19_v2(dom, dow):
    start = 1901
    end = 2001
    count = 0

    while start < end:
        for i in xrange(1, 13):
            date = datetime(start, i, dom)
            if date.weekday() == dow:
                count += 1

        start += 1

    return count


def main():
    #print("Hello World!")
    print(problem19(1, 6))


main()



