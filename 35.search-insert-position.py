#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while (left <= right):
            middle = (left+right)//2
            print("left:",left)
            print("right:",right)
            print("middle:",middle)
            if (nums[middle] < target):
                left = middle + 1
            elif (nums[middle] > target):
                right = middle - 1
            else:
                return middle
        return right + 1

s = Solution()
print(s.searchInsert([1,3,5,6],2))
        

        
# @lc code=end

