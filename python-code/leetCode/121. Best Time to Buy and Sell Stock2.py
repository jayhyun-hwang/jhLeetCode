# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = prices[0], prices[0]
        max_profit = 0
        for price in prices:
            if buy - price > 0:
                buy = price
                sell = 0
            sell = max(sell, price)
            max_profit = max(max_profit, sell - buy)
            # print(buy, sell, max_profit)

        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(s.maxProfit([7, 11, 1, 2, 4]))  # 4
