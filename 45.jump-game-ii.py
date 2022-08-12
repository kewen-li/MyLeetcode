#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (37.38%)
# Likes:    9109
# Dislikes: 325
# Total Accepted:    674.4K
# Total Submissions: 1.8M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# You can assume that you can always reach the last index.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,3,0,1,4]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        curDistance = 0
        nextDistance = 0
        step = 0
        for i in range(len(nums)):
            nextDistance = max(nextDistance, i + nums[i])
            if (i == curDistance):
                if (curDistance != len(nums) - 1):
                    step += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1:
                        break
            
        return step
# @lc code=end

