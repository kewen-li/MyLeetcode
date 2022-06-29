#
#
# @lc app=leetcode id=1 lang=python3
# [1] Two Sum
#

# @lc code=start
from typing import List

# Two-Pointer
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if (nums[i]+nums[j]) == target:
#                     return [i,j]


# Hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            res = target - nums[i]
            print(res)
            if res in d:
                print(d)
                return [d[res], i]
            d[nums[i]] = i


s = Solution()
print(s.twoSum([3, 2, 4], 6))
# @lc code=end
