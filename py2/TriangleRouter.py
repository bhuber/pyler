#!/usr/local/bin/python

"""
TriangleRouter - for finding max routes in triangle arrays
Used in problems 18, 67
"""

import math


class TriangleRouter(object):
    #Array of arrays, parallel with original data
    #each element is (original value, value max-path route for all child nodes, index of child node with greatest path)
    _data = None

    def __init__(self, data):
        self._data = map(lambda a: [float(a), float(a), -1], data)

    def find_max_route(self):
        for i in xrange(len(self._data) - 1, -1, -1):
            #pdb.set_trace()
            node = self._data[i]

            p_idx = TriangleRouter.get_left_parent(i)
            if not (p_idx is None):
                p = self._data[p_idx]
                max_route = node[1] + p[0]

                if max_route > p[1]:
                    p[1] = max_route
                    p[2] = i

            p_idx = TriangleRouter.get_right_parent(i)
            if not (p_idx is None):
                p = self._data[p_idx]
                max_route = node[1] + p[0]

                if max_route > p[1]:
                    p[1] = max_route
                    p[2] = i

        return self._data[0][1]
    
    @staticmethod
    def get_left_child(array, i):
        """
        Given a triangular array and index, returns the left child of the index, or None if it doesn't exist
        """
        # 0 | 1 2 | 3 4 5 | 6 7 8 9 | 10 11 12 13 14 |
        length = len(array)
        tri = TriangleRouter.lower_triangle_rank(i)
        left = length + tri
        return left if left < length else None

    @staticmethod
    def get_right_child(array, i):
        """
        Given a triangular array and index, returns the right child of the index, or None if it doesn't exist
        """
        length = len(array)
        tri = TriangleRouter.lower_triangle_rank(i)
        left = length + tri + 1
        return left if left < length else None

    @staticmethod
    def get_left_parent(i):
        """
        Given a triangular array and index, returns the left parent of the index, or None if it doesn't exist
        """
        if i < 2:
            return None

        tri = TriangleRouter.lower_triangle_rank(i)
        idx = i - tri - 1
        if TriangleRouter.lower_triangle_rank(idx) < tri - 1:
            return None
        else:
            return idx;

    @staticmethod
    def get_right_parent(i):
        """
        Given a triangular array and index, returns the right parent of the index, or None if it doesn't exist
        """
        if i < 1:
            return None

        tri = TriangleRouter.lower_triangle_rank(i)
        idx = i - tri
        if TriangleRouter.lower_triangle_rank(idx) > tri - 1:
            return None
        else:
            return idx;

    @staticmethod
    def lower_triangle_rank(t):
        """
        returns the rank of the greatest triangular number <= t
        i.e. if you round t down to the nearest triangular number which is the nth triangular number, it returns n
        """

        # let t = n * (n + 1) / 2 = (n^2 + n) / 2
        # (1/2) * (n^2) + (1/2) * n - t = 0
        # n = (-0.5 +- sqrt((1/4) + 2t)) = sqrt((8t + 1) / 4) - 1/2 = (sqrt(8t + 1) - 1) / 2
        n = (math.sqrt(8 * t + 1) - 1) / 2
        n = math.floor(n)
        return int(n)
        


