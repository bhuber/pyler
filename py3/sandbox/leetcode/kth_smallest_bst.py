# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int):
        return self.kth_smallest_internal(root, k - 1)[1] if k > 0 else None

    def kth_smallest_internal(self, root: Optional[TreeNode], k: int) -> (int, object):
        """
        Returns (number of nodes searched, None) if n_searched < k, or (None, result) if
        the result was found
        """

        if root is None:
            return 0, None
        k_diff_left, maybe_result = self.kth_smallest_internal(root.left, k)

        if k_diff_left is None:
            # found result in left, bubble up
            return k_diff_left, maybe_result

        new_k = k - k_diff_left
        if new_k == 0:
            # we're the result, return
            return None, root.val
        elif new_k < 0:
            raise RuntimeError(f"Should never end up with negative new_k, value was {new_k}")

        k_diff_right, maybe_result = self.kth_smallest_internal(root.right, new_k - 1)
        if k_diff_right is None:
            # found result in right, bubble up
            return k_diff_right, maybe_result

        new_k -= k_diff_right
        if new_k < 0:
            raise RuntimeError(f"Should never end up with negative new_k, value was {new_k}")

        return (k_diff_left + 1 + k_diff_right), None
