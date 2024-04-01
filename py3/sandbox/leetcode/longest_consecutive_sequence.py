# https://leetcode.com/problems/longest-consecutive-sequence/
from collections import defaultdict
from typing import List, Dict


class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        # max longest sequence is len(nums) = n
        # Ergo, if two integers are more than (n - 1) apart, they can't be in the same sequence
        # Create dict, key is a range [x*n, (x + 1)*n - 1), value is list of elements that appear in that range
        # find m = max(v) for v in dict
        # for each v in dict where len(v) > m / 2 and v is candidate solution:
        #     check if previous or next range is in dict, and see if it can be combined
        #     Update best candidate solution

        n = len(nums)
        range_buckets: Dict[IntRange, IntSet] = {}
        for i in nums:
            range_key = IntRange.range_for_int_and_stride(i, n)
            current_bucket = range_buckets.get(range_key, None)
            if current_bucket is None:
                current_bucket = IntSet(range_key.start, range_key.end)
                range_buckets[range_key] = current_bucket

            current_bucket.add(i)

        print(range_buckets)

        max_bucket_len = max(len(v) for v in range_buckets.values())
        if max_bucket_len <= 2:
            # easy optimization for when all numbers are far apart
            return max_bucket_len

        best_range_len = 0
        for k, v in range_buckets.items():
            if len(v) <= max_bucket_len // 2:
                continue

            current_range_len = 0
            if k.end - 1 in v:
                next_range = range_buckets[k.next_range()]
                if k.end in next_range:
                    current_range_len = len(v) + len(next_range)

            if current_range_len == 0:
                current_range_len = len(v)
            if current_range_len > best_range_len:
                best_range_len = current_range_len

        return best_range_len

    def longestConsecutive(self, nums: List[int]) -> int:
        marked_nums: Dict[int, IntWithMark] = dict((i, IntWithMark(i)) for i in nums)
        longest_seq = 0
        for k, v in marked_nums.items():
            if v.mark:
                continue
            curr_seq = 1

            # look ahead
            curr_item = marked_nums.get(k + 1, None)
            while curr_item is not None:
                curr_seq += 1
                curr_item.mark = True
                curr_item = marked_nums.get(curr_item.val + 1, None)

            # look behind
            curr_item = marked_nums.get(k - 1, None)
            while curr_item is not None:
                curr_seq += 1
                curr_item.mark = True
                curr_item = marked_nums.get(curr_item.val - 1, None)

            if curr_seq > longest_seq:
                longest_seq = curr_seq

        return longest_seq


class IntWithMark:
    def __init__(self, val):
        self.val = val
        self.mark = False


class IntSet:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self._elements = [False for i in range(start, end)]
        self._length = 0

    def add(self, i: int):
        if not (self.start <= i < self.end):
            raise IndexError(f"i ({i}) must be in the range [{self.start}, {self.end})")

        idx = i - self.start
        if not self._elements[idx]:
            self._length += 1
        self._elements[idx] = True

    def __contains__(self, item):
        return type(item) is int and (self.start <= item < self.end) and self._elements[item - self.start]

    def __getitem__(self, item):
        return self.__contains__(item)

    def get_without_offset(self, i):
        if not (self.start <= i + self.start < self.end):
            raise IndexError(f"i ({i}) must be in the range [{0}, {self.end - self.start})")

        return self._elements[i]

    def __len__(self):
        return self._length


class IntRange:
    def __init__(self, start: int, end: int):
        # start inclusive, end exclusive
        assert start <= end
        self.start = start
        self.end = end
        self._hash = hash((self.start, self.end))

    def next_range(self):
        return IntRange(self.end, self.end + (self.end - self.start))

    def prev_range(self):
        return IntRange(self.start - (self.end - self.start), self.start)

    @staticmethod
    def range_for_int_and_stride(i: int, stride: int):
        start = stride * (i // stride)
        return IntRange(start, start + stride)

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return self._hash

    def __str__(self):
        return f"IntRange({self.start}, {self.end})"

    def __repr__(self):
        return self.__str__()

