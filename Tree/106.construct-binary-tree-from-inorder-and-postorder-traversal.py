#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (55.65%)
# Likes:    4954
# Dislikes: 75
# Total Accepted:    420.9K
# Total Submissions: 745.6K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
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
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    #后序数组的最后一个元素为切割点，先切中序数组，根据中序数组，反过来在切后序数组。一层一层切下去，每次后序数组最后一个元素就是节点元素。
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        
        # 1. Get Root Value
        rootVal = postorder[-1]
        root = TreeNode(rootVal)

        # 2. Seperator Index
        sepIndex = inorder.index(rootVal)

        # 3. Slice InOrder List
        inorder_left = inorder[:sepIndex]
        inorder_right = inorder[sepIndex+1:]

        # 4. Slice PostOrder List
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left) : len(postorder)-1]
        
        # 5. Recursion
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

# @lc code=end

