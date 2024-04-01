from unittest import TestCase

from leetcode.longest_consecutive_sequence import IntRange, Solution


class TestIntRange(TestCase):
    def test_next_range(self):
        r1 = IntRange(1, 3)
        self.assertEqual(IntRange(3, 5), r1.next_range())
        self.assertEqual(hash(IntRange(3, 5)), hash(r1.next_range()))

        r1 = IntRange(1, 1)
        self.assertEqual(IntRange(1, 1), r1.next_range())
        self.assertEqual(hash(IntRange(1, 1)), hash(r1.next_range()))

    def test_prev_range(self):
        r1 = IntRange(3, 5)
        self.assertEqual(IntRange(1, 3), r1.prev_range())
        self.assertEqual(hash(IntRange(1, 3)), hash(r1.prev_range()))

        r1 = IntRange(1, 1)
        self.assertEqual(IntRange(1, 1), r1.prev_range())
        self.assertEqual(hash(IntRange(1, 1)), hash(r1.prev_range()))

    def test_range_for_int_and_stride(self):
        self.assertEqual(
            IntRange(0, 3),
            IntRange.range_for_int_and_stride(0, 3))
        self.assertEqual(
            IntRange(0, 3),
            IntRange.range_for_int_and_stride(1, 3))
        self.assertEqual(
            IntRange(0, 3),
            IntRange.range_for_int_and_stride(2, 3))
        self.assertEqual(
            IntRange(3, 6),
            IntRange.range_for_int_and_stride(3, 3))


class TestSolution(TestCase):
    def test_longest_consecutive(self):
        s = Solution()
        self.assertEqual(4,
                         s.longestConsecutive([100, 4, 200, 1, 3, 2]))
        self.assertEqual(9,
                         s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
        self.assertEqual(0, s.longestConsecutive([]))
        self.assertEqual(1, s.longestConsecutive([1]))
        self.assertEqual(1, s.longestConsecutive([1, 3]))
        self.assertEqual(2, s.longestConsecutive([1, 2]))
        self.assertEqual(2, s.longestConsecutive([2, 1]))
        self.assertEqual(6, s.longestConsecutive([7, 8, 9, 10, 11, 12, 19, 20, 21, 22]))
