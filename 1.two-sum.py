#
#
# @lc app=leetcode id=1 lang=python3
# [1] Two Sum
#

# @lc code=start
from typing import List

### Two-Pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):    
                if (nums[i]+nums[j]) == target:
                    return [i,j]


### Hash table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
        
        
# @lc code=end
                
