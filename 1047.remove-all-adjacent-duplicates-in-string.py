#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (71.00%)
# Likes:    3554
# Dislikes: 165
# Total Accepted:    303K
# Total Submissions: 427.5K
# Testcase Example:  '"abbaca"'
#
# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing
# them.
# 
# We repeatedly make duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made. It
# can be proven that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
# 
# 
# Example 2:
# 
# 
# Input: s = "azxxzy"
# Output: "ay"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start

# Method1: Stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for item in s:
            if stack and item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)

# @lc code=end

