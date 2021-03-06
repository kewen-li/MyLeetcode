#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Easy (62.84%)
# Likes:    4413
# Dislikes: 135
# Total Accepted:    1000K
# Total Submissions: 1.6M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
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

# Recursion
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def traversal(root: TreeNode):
#             if not root:
#                 return
#             result.append(root.val)  # Root
#             traversal(root.left)  # Left
#             traversal(root.right)  # Right
#         traversal(root)
#         return result


# Loop
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        s = []
        if root:
            s.append(root)
        while s:
            node = s.pop()
            if node:
                # 右左中
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
                s.append(node)
                s.append(None)

            else:
                node = s.pop()
                result.append(node.val)
        return result
        
# @lc code=end

