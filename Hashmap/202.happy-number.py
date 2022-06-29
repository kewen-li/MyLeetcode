#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (53.40%)
# Likes:    5783
# Dislikes: 742
# Total Accepted:    852K
# Total Submissions: 1.6M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculateHappy(num):
            sum = 0
            while num:
                sum += (num % 10) ** 2
                num = num // 10

            return sum

        record = set()
        while True:
            n = calculateHappy(n)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)


s = Solution()
print(s.isHappy(19))

# @lc code=end
