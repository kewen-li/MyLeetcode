#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (42.92%)
# Likes:    3403
# Dislikes: 656
# Total Accepted:    448.2K
# Total Submissions: 1M
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.
#
# Note that division between two integers should truncate toward zero.
#
# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.
#
#
# Example 1:
#
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#
# Constraints:
#
#
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
#
#
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:  # 不要用isdigit(),-11 不行
                stack.append(item)
            else:
                d1, d2 = stack.pop(), stack.pop()
                stack.append(int(eval(f'{d2}{item}{d1}')))
        return int(stack.pop())

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# @lc code=end
