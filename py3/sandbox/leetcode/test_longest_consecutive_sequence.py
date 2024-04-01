from unittest import TestCase

from leetcode.longest_consecutive_sequence import Solution


class TestSolution(TestCase):
    def test_longest_consecutive(self):
        s = Solution()
        self.assertEqual(4,
                         s.longestConsecutive([100, 4, 200, 1, 3, 2]))
        self.assertEqual(9,
                         s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
        self.assertEqual(0, s.longestConsecutive([]))
        self.assertEqual(1, s.longestConsecutive([1]))
        self.assertEqual(1, s.longestConsecutive([1, 3]))
        self.assertEqual(2, s.longestConsecutive([1, 2]))
        self.assertEqual(2, s.longestConsecutive([2, 1]))
        self.assertEqual(6, s.longestConsecutive([7, 8, 9, 10, 11, 12, 19, 20, 21, 22]))
