# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# import heapq


# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         min_heap = []

#         max_profit = 0
#         for idx, val in enumerate(prices):
#             if idx+1 >= len(prices):
#                 continue
#             # print(prices[idx+1:])
#             heapq.heappush(min_heap, val)
#             max_heap = prices[idx+1:]
#             max_heap = [-x for x in max_heap]
#             heapq.heapify(max_heap)

#             # print(max_heap, min_heap)
#             diff = -max_heap[0] - min_heap[0]
#             max_profit = max_profit if diff < max_profit else diff

#         return max_profit
import heapq


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_heap = []
        max_heap = []
        num_count = dict()
        for val in prices:
            if val not in num_count:
                num_count[val] = 0
            num_count[val] += 1
            heapq.heappush(max_heap, -val)

        max_profit = 0
        for val in prices:
            if len(max_heap) < 1:
                break
            heapq.heappush(min_heap, val)
            temp_min = min_heap[0]
            num_count[val] -= 1
            temp_max = 0
            while True:
                if len(max_heap) < 1:
                    break
                temp_max = -heapq.heappop(max_heap)
                # print(min_heap, max_heap, num_count, temp_max)
                if num_count[temp_max] < 1:
                    continue
                else:
                    heapq.heappush(max_heap, -temp_max)
                    break
            diff = temp_max - temp_min
            max_profit = max_profit if diff < max_profit else diff

        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(s.maxProfit([7, 11, 1, 2, 4]))  # 4
