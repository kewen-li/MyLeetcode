#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (65.40%)
# Likes:    2324
# Dislikes: 224
# Total Accepted:    182.5K
# Total Submissions: 277.4K
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
    def __init__(self, val=0, left=None, right=None ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left = None
        from collections import deque
        que = deque([root])
        
        while que:
            left = que[0].val
            for _ in range(len(que)):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return left
# @lc code=end

