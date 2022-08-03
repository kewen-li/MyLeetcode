#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (49.16%)
# Likes:    5930
# Dislikes: 164
# Total Accepted:    299.3K
# Total Submissions: 604K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
# 
# Basically, the deletion can be divided into two stages:
# 
# 
# Search for a node to remove.
# If the node is found, delete the node.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and
# delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's
# also accepted.
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# 
# 
# Example 3:
# 
# 
# Input: root = [], key = 0
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5
# 
# 
# 
# Follow up: Could you solve it with time complexity O(height of tree)?
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1. No Deletion
        if not root: 
            return root
        if root.val == key:
            # 2. No Children
            if not root.left and not root.right:
                del root
                return None
            # 3. No Left
            if not root.left and root.right:
                tmp = root
                root = root.right
                del tmp
                return root
            # 4. No Right
            if root.left and not root.right:
                tmp = root
                root = root.left
                del tmp 
                return root

            # 5. Both Children
            else:
                newloc = root.right
                while newloc.left:
                    newloc = newloc.left
                newloc.left = root.left
                tmp = root
                root = root.right
                del tmp 
                return root

        if root.val < key: 
            root.right = self.deleteNode(root.right, key)
        if root.val > key: 
            root.left = self.deleteNode(root.left, key)
        return root
            
                
# @lc code=end

