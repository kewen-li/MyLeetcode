#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (47.42%)
# Likes:    2318
# Dislikes: 586
# Total Accepted:    161.8K
# Total Submissions: 337.6K
# Testcase Example:  '[1,null,2,2]'
#
# Given the root of a binary search tree (BST) with duplicates, return all the
# mode(s) (i.e., the most frequently occurred element) in it.
# 
# If the tree has more than one mode, return them in any order.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# 
# Input: root = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        pre = None
        stack = []
        maxCount, count = 0, 0
        result = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre is None:  # First Node
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1
                if count == maxCount:
                    result.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    result.clear()
                    result.append(cur.val)
                pre = cur
                cur = cur.right

        return result
            
        
# @lc code=end

