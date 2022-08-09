#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (55.61%)
# Likes:    5289
# Dislikes: 322
# Total Accepted:    426.1K
# Total Submissions: 756.7K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = []
# Output: 0
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = 0
        r = 0
        left = root.left
        right = root.right
        while left:
            left = left.left
            l += 1
        while right:
            right = right.right
            r += 1

        if l == r:
            print(l,r)
            return (2 << l) - 1

        leftNumber = self.countNodes(root.left)
        rightNumber = self.countNodes(root.right)
        return leftNumber + rightNumber + 1

# @lc code=end
