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
            print("left:",left)
            print("right:",right)
            print("middle:",middle)
            if (middle*middle) < x:
                left = middle+1
            elif (middle*middle) > x:
                right = middle-1
            else:
                return middle
        return left
                
s = Solution()
print(s.mySqrt(8))
        
# @lc code=end

