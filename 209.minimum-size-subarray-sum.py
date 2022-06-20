#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (43.56%)
# Likes:    6857
# Dislikes: 197
# Total Accepted:    545.8K
# Total Submissions: 1.2M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
# numsr-1, numsr] of which the sum is greater than or equal to target. If there
# is no such subarray, return 0 instead.
# 
# 
# Example 1:
# 
# 
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
# 
# 
# Example 2:
# 
# 
# Input: target = 4, nums = [1,4,4]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#

# @lc code=start
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        sum = 0
        result = float('inf')
        for fast in range(len(nums)):
            sum += nums[fast]
            while (sum >= target):
                sublength = (fast-slow+1)
                print(nums[fast],nums[slow],sublength)
                if sublength < result:  result = sublength
                sum -=  nums[slow]
                slow += 1

        return 0 if result==float('inf') else result 
                
        

s = Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))
print(s.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))
# @lc code=end

