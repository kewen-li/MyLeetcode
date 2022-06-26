#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while (left <= right):
            middle = (left+right)//2
            if (middle*middle) <= x < (middle+1)*(middle+1):
                return middle 
            elif (middle*middle) > x:
                right = middle-1
            else:
                left = middle+1
                
s = Solution()
print(s.mySqrt(26))
        
# @lc code=end

