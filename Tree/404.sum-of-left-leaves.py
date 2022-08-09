#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (55.30%)
# Likes:    3568
# Dislikes: 253
# Total Accepted:    369.3K
# Total Submissions: 663.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the sum of all left leaves.
# 
# A leaf is a node with no children. A left leaf is a leaf that is the left
# child of another node.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and
# 15 respectively.
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
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
        self.val = 0
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftval = self.sumOfLeftLeaves(root.left)
        rightval = self.sumOfLeftLeaves(root.right)

        midval = 0
        if (root.left and not root.left.left and not root.left.right):
            midval = root.left.val
        
        return midval + leftval + rightval

# class Solution:
#     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         # does this node have a left child which is a leaf?
#         if root.left and not root.left.left and not root.left.right:
# 			# gotcha
#             return root.left.val + self.sumOfLeftLeaves(root.right)

#         # no it does not have a left child or it's not a leaf
#         else:
# 			# bummer
#             return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
# @lc code=end

