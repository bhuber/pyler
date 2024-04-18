from unittest import TestCase

from leetcode.kth_smallest_bst import TreeNode, Solution


# def construct_tree(e):
#     if isinstance(e, dict):
#         return TreeNode(**dict)
#     else:
#         return TreeNode(e)

def construct_tree(items, idx=0):
    l = len(items)
    if idx >= l or items[idx] is None:
        return None
    else:
        return TreeNode(items[idx], construct_tree(items, idx*2 + 1), construct_tree(items, idx*2 + 2))

class TestSolution(TestCase):
    def test_kth_smallest_1(self):
        s = Solution()

        self.assertEqual(None, s.kthSmallest(None, 0))
        self.assertEqual(None, s.kthSmallest(None, 1))

        undertest = construct_tree([3,1,4,None,2])
        self.assertEqual(1, s.kthSmallest(undertest, 1))

        undertest = construct_tree([5,3,6,2,4,None,None,1])
        self.assertEqual(1, s.kthSmallest(undertest, 1))
        self.assertEqual(2, s.kthSmallest(undertest, 2))
        self.assertEqual(3, s.kthSmallest(undertest, 3))
        self.assertEqual(4, s.kthSmallest(undertest, 4))
        self.assertEqual(5, s.kthSmallest(undertest, 5))
        self.assertEqual(6, s.kthSmallest(undertest, 6))

        undertest = construct_tree([5])
        self.assertEqual(5, s.kthSmallest(undertest, 1))
        self.assertEqual(None, s.kthSmallest(undertest, 2))
