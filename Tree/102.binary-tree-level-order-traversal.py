#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (61.16%)
# Likes:    8976
# Dislikes: 173
# Total Accepted:    1.3M
# Total Submissions: 2.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
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
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# Loop
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         result = []
#         if not root:
#             return result

#         from collections import deque
#         queue = deque([root])

#         while queue:
#             size = len(queue)
#             temp = []
#             for _ in range(size):
#                 cur = queue.popleft()
#                 temp.append(cur.val)
#                 if cur.left:
#                     queue.append(cur.left)
#                 if cur.right:
#                     queue.append(cur.right)
#             result.append(temp)
#         return result

# Recursion
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def traversal(root, depth):
            if not root: 
                return []
            if len(result) == depth:  
                result.append([])
            result[depth].append(root.val)
            if root.left:
                traversal(root.left, depth + 1)
            if root.right:
                traversal(root.right, depth + 1)

        traversal(root, 0)
        return result



# @lc code=end
