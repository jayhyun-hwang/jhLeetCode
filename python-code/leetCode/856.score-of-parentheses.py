#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        answer = 0
        stack = []
        for ele in s:
            if ele == "(":
                stack.append(ele)
                continue
            vertex = stack.pop()
            if vertex == "(":
                stack.append(1)
                continue
            temp_num = vertex
            while vertex != "(":
                vertex = stack.pop()
                if vertex == "(":
                    temp_num *= 2
                    stack.append(temp_num)
                else:
                    temp_num += vertex

        answer = sum(stack)
        return answer

# @lc code=end
