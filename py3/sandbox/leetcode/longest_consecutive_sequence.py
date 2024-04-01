# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List, Dict


class Solution:
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
