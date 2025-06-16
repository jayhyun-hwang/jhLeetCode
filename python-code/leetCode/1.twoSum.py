# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for idx, val in enumerate(nums):
            if val not in num_map:
                num_map[val] = []
            num_map[val].append(idx)
        for i, v in enumerate(nums):
            diff = target - v
            if diff not in num_map:
                continue
            for j in num_map[diff]:
                if i == j:
                    continue
                return [i, j]
        return []


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # 2
# nums = [2,7,11,15], target = 9
