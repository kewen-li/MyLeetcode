#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (64.48%)
# Likes:    4475
# Dislikes: 143
# Total Accepted:    761.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def traversal(root: TreeNode):
#             if not root:
#                 return
#             traversal(root.left)  # Left
#             traversal(root.right)  # Right
#             result.append(root.val)  # Root
#         traversal(root)
#         return result

# Loop
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        s = []
        if root:
            s.append(root)
        while s:
            node = s.pop()
            if node:
                # 中右左
                s.append(node)
                s.append(None)
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
            else:
                node = s.pop()
                result.append(node.val)
        return result

            
# @lc code=end

