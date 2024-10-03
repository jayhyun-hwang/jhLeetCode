#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in reversed(matrix):
            if row[0] > target:
                continue
            for col in row:
                if col == target:
                    return True
        return False
# @lc code=end
