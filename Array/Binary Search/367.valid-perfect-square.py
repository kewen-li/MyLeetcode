#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while (left<=right):
            middle =  (left+right)//2
            if (middle*middle) < num:
                left = middle +1
            if (middle*middle) > num:
                right = middle -1
            if (middle*middle) == num:
                return True

        return False
        
# @lc code=end

