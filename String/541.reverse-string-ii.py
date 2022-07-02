#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (50.20%)
# Likes:    1047
# Dislikes: 2505
# Total Accepted:    157.6K
# Total Submissions: 314K
# Testcase Example:  '"abcdefg"\n2'
#
# Given a string s and an integer k, reverse the first k characters for every
# 2k characters counting from the start of the string.
# 
# If there are fewer than k characters left, reverse all of them. If there are
# less than 2k but greater than or equal to k characters, then reverse the
# first k characters and leave the other as original.
# 
# 
# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        while left < len(s):
            right = left + k
            s = s[:left] + s[left:right][::-1] + s[right:]
            left = left + 2 * k
        return s
# @lc code=end

