#!/usr/bin/python


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

    total = b ** n
    found = [0 for _ in range(total)]
    nd = 0
    nf = 0
    result = [0 for _ in xrange(n - 1)]
    current = [0 for _ in xrange(n - 1)]
    offset = 0
    sanity = 0

    while nf < total:
        if sanity > b:
            raise Exception("Infinite loop encountered, bailing")

        nd = find_next_free_digit(b, current, found, offset)
        if nd < 0:
            if nd >= total:
                return result
            else:
                raise Exception("Ooops, algorithm failed, couldn't find next digit")

        temp = current[1:]
        temp.append(nd)
        la1 = find_next_free_digit(b, temp, found)
        if la1 < 0 and nf < total - 1:
            #import ipdb; ipdb.set_trace()
            offset += 1
            sanity += 1
            continue
        else:
            current.append(nd)
            result.append(nd)
            found[digits_to_num(b, current)] += 1
            nf += 1
            current = temp
            sanity = 0
            offset = 0

    return result


if __name__ == 'main':
    print("Testing for base 3, digits 2")
    print(combo_string(3, 2))

