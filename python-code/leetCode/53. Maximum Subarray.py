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
    def maxSubArray(self, nums):
        res_list = [0] * (len(nums) + 1)
        for idx, val in enumerate(nums):
            res_list[idx + 1] = res_list[idx] + val
        return max(res_list)

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([1]))
print(solution.maxSubArray([5,4,-1,7,8]))
