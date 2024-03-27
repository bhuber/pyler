#!/usr/local/bin/python

"""
Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.


How many routes are there through a 2020 grid?
"""

"""
Let f(n, m) be the number of routes for an nxm grid
it's obvious f(n, m) == f(m, n)
for all n < 0, m < 0: f(n, m) = 0
f(0, 0) = 0
f(n, 0) = 1
f(0, m) = 1
f(n, m) = f(n - 1, m) + f(n, m - 1)

"""

routes = { }

def make_key(n, m):
    return "%s:%s" % (n, m)

def grid_routes(n, m):
    if n < 0 or m < 0:
        return 0
    elif n == 0:
        return 0 if m == 0 else 1
    elif m == 0:
        return 0 if n == 0 else 1
    else:
        first = None
        second = None
        key = make_key(n - 1, m)

        if routes.has_key(key):
            first = routes[key]
        else:
            first = grid_routes(n - 1, m)

        key = make_key(n, m - 1)
        if routes.has_key(key):
            second = routes[key]
        else:
            second = grid_routes(n, m - 1)
    
        result = first + second
        key = make_key(n, m)
        routes[key] = result
        return result

def main():
    #print("Hello World!")
    print(grid_routes(20, 20))


main()



