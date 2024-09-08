from math import inf
class Solution:
    # def maxSubArray(self, nums):
    #     if len(nums) < 2:
    #         return nums.pop()
    #     max_sum = -99999
    #     last = len(nums) - 1
    #     for i, v in enumerate(nums):
    #         temp_sum = 0
    #         for idx in range(i, last + 1):
    #             temp_sum += nums[idx]
    #             if temp_sum > max_sum:
    #                 max_sum = temp_sum
    #     return max_sum
    # def maxSubArray(self, nums):
    #     cur_sum = 0
    #     max_sum = -inf
    #     for n in nums:
    #         cur_sum = max(cur_sum + n, n)
    #         max_sum = max(max_sum, cur_sum)
    #     return max_sum
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        acc = [0] * len(nums)
        acc[0] = nums[0]
        for idx in range(1, len(nums)):
            acc[idx] = max(acc[idx - 1] + nums[idx], nums[idx])
        return max(acc)


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 2
print(solution.maxSubArray([1]))  # 1
print(solution.maxSubArray([5, 4, -1, 7, 8]))  # 23
