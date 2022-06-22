#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (65.15%)
# Likes:    3754
# Dislikes: 182
# Total Accepted:    370.2K
# Total Submissions: 566.8K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0]*n for _ in range(n)]
        startx,starty = 0,0
        loop, mid = n//2, n//2
        count = 1                    ## Count number 
        for offset in range(1,loop+1):
            ## left to right
            for i in range(startx,n-offset):
                #print("left to right", startx,i)
                nums[startx][i] =  count
                count +=1
            ## right to down
            for i in range(starty, n-offset):
                #print("right to down", i, n-1)
                nums[i][n-offset] = count
                count += 1
            ## down to left
            for i in range(n-offset,startx,-1):
                #print("down to left", n-1,i)
                nums[n-offset][i] = count
                count += 1
            ## left to up
            for i in range(n-offset,starty,-1):
                #print("left to up", i,starty)
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

s = Solution()
print(s.generateMatrix(1))
print(s.generateMatrix(4))
# @lc code=end

