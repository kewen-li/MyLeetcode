#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (69.26%)
# Likes:    3107
# Dislikes: 1940
# Total Accepted:    688.2K
# Total Submissions: 990.8K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
#
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
#
#
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1dict = {}
        for i in nums1:
            nums1dict[i] = 1 + nums1dict.get(i, 0)
        for i in nums2:
            if nums1dict.get(i, 0) > 0 and i not in result:
                result.append(i)
        return result


s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))

# @lc code=end
