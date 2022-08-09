#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (58.95%)
# Likes:    4472
# Dislikes: 196
# Total Accepted:    535.9K
# Total Submissions: 900.2K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: ["1"]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
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
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = ''
        result = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    
    def traversal(self, root, path, result):
        path += str(root.val)
        if (root.left is None and root.right) is None:
            result.append(path)
        if root.left:
            self.traversal(root.left, path + '->', result)
        if root.right:
            self.traversal(root.right, path + '->', result)
# @lc code=end

