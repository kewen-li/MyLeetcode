#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (65.03%)
# Likes:    9746
# Dislikes: 385
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#

# @lc code=start
from typing import List
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计
        frequency = {}
        for item in nums:
            frequency[item] = frequency.get(item, 0) + 1

        # 定义小顶堆
        pri_que = []
        for key, item in frequency.items():
            heappush(pri_que, (item, key))
            if len(pri_que) > k:
                heappop(pri_que)

        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heappop(pri_que)[1]
        return result


# @lc code=end
