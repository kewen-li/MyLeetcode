#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def FindBoarder(nums, target, leftOrRight):  # True for left, False for Right
            left, right = 0, len(nums)-1
            index = -1
            while (left <= right):
                middle = (left+right)//2
                if target > nums[middle]:
                    left = middle + 1
                elif target < nums[middle]:
                    right = middle - 1
                else:
                    index = middle
                    if leftOrRight:
                        right = middle-1
                    else:
                        left = middle + 1
            return index
        
        leftPos, rightPos = FindBoarder(nums,target,True),FindBoarder(nums,target,False)
        return [leftPos,rightPos]


s = Solution()
print(s.searchRange([5, 5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([1, 2, 3, 6, 7, 7, 7, 7, 10], 7))

# @lc code=end
