#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (58.00%)
# Likes:    10363
# Dislikes: 280
# Total Accepted:    811K
# Total Submissions: 1.4M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # 1. Get Root Value
        rootVal = preorder[0]
        root = TreeNode(rootVal)

        # 2. Separator Index
        sepIndex = inorder.index(rootVal)

        # 3. Slice Inorder List
        inorder_left = inorder[:sepIndex]
        inorder_right = inorder[sepIndex+1:]

        # 4. Slice Postorder List
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        # Recursion
        root.left = self.buildTree(preorder_left, inorder_left, )
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
# @lc code=end
