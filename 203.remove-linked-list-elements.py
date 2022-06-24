#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (43.70%)
# Likes:    5215
# Dislikes: 169
# Total Accepted:    730.9K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [], val = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [7,7,7,7], val = 7
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class ListNode:
    def __init__(self, val=0 ,next=None) -> None:
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next =head)
        mynode = dummy
        while mynode.next != None:
            if mynode.next.val == val:
                mynode.next = mynode.next.next
            else:
                mynode = mynode.next
        return dummy.next
        # dummy 1 4 2 1
# @lc code=end

 