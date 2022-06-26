#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (39.16%)
# Likes:    10775
# Dislikes: 543
# Total Accepted:    780.4K
# Total Submissions: 2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#

# @lc code=start

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        substring = ""
        slow = 0
        match = 0
        tlist = collections.Counter(t) ##  ABC: {'A':1,'B':1,'C':1}
        
        for fast,char in enumerate(s):
            if char in tlist:
                if tlist[char]==1: match += 1
                tlist[char] -=1
            while match == len(tlist):
                substring = s[slow:fast+1]
                if result == "": result = substring
                result = min(substring,result,key=len)
                if s[slow] in tlist:
                    tlist[s[slow]] += 1
                    if tlist[s[slow]] > 0: match-=1
                slow += 1
        return result
# @lc code=end

s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))

