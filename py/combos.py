#!/usr/bin/python

"""
Our building is secured by locked doors with keypads. The keypads have 10 digits
on them (0 - 9) and require a 4-digit access code to unlock the doors.
Unfortunately, they were designed by Bob the Bungler, so rather than typing 4
digits and hitting "Enter", they simply wait for the right sequence of digits to
be pressed and then unlock. So for example if the code is "1234", and someone
enters "2938470871234" it will open on the last digit. What is the minimum
number of digits you have to enter to try all possible combinations?
"""


def digits_to_num(b, digits):
    """Given a list of digits in base b returns the actual number they represent"""
    return sum([d * (b ** e) for (d, e) in zip(digits, xrange(len(digits) - 1, -1, -1))])


def find_next_free_digit(b, digits, found, offset=0):
    """
    Finds the next digit we can use, -1 if none available
    b:      base we're working in
    d:      first n - 1 digits
    found:  array of numbers we've found so far
    offset:  offset to start looking at
    """

    assert len(found) == b ** (len(digits) + 1), "Bad inputs for find_next_free_digit!"

    temp = list(digits)
    temp.append(0)
    start = digits_to_num(b, temp)

    for i in xrange(b):
        idx = (i + offset) % b
        if found[start + idx] == 0:
            return idx

    return -1


def combo_string(b, n):
    """
    Returns a sequence of digits in base b covering all combinations of n digits
    b:  The base we're working in
    n:  The number of digits in an entry in base b
    """

    def to_digits(d):
        return [i['digit'] for i in d]

    total = b ** n
    found = [0 for _ in range(total)]
    nd = 0
    nf = 0
    result = [{ 'digit': 0, 'next_try': 0 } for _ in xrange(n - 1)]

    while nf < total:
        #import ipdb; ipdb.set_trace()
        if result[-1]['next_try'] == b:
            # Tried all our digits, backtrack
            found[digits_to_num(b, to_digits(result[-n:]))] -= 1
            nf -= 1
            result.pop()
            result[-1]['next_try'] += 1
            continue

        current = [i['digit'] for i in result[1 - n:]]
        nd = find_next_free_digit(b, current, found, result[-1]['next_try'])
        if nd < 0:
            if nf >= total:
                return result
            else:
                # backtrack
                found[digits_to_num(b, to_digits(result[-n:]))] -= 1
                nf -= 1
                result.pop()
                result[-1]['next_try'] += 1
                continue

        result.append({ 'digit': nd, 'next_try': 0 })
        current.append(nd)
        found[digits_to_num(b, current)] += 1
        nf += 1

    return [i['digit'] for i in result]


if __name__ == 'main':
    print("Testing for base 3, digits 2")
    print(combo_string(3, 2))

