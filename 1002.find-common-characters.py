#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (68.43%)
# Likes:    2415
# Dislikes: 197
# Total Accepted:    148.6K
# Total Submissions: 217.3K
# Testcase Example:  '["bella","label","roller"]'
#
# Given a string array words, return an array of all characters that show up in
# all strings within the words (including duplicates). You may return the
# answer in any order.
#
#
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
#
#
#

# @lc code=start
import collections
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        result = list()
        chars = collections.Counter(words[0])
        for i in range(1, len(words)):
            chars = chars & collections.Counter(words[i])
        for c in chars:
            while (chars[c]):
                result.append(c)
                chars[c] -= 1
        return result


# @lc code=end
