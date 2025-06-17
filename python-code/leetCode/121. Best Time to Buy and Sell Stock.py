# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def hammingWeight(self, n: int) -> int:
        q = n
        bits = 0
        while q >= 1:
            r = q % 2
            if r == 1:
                bits += 1
            q = q // 2
        return bits


s = Solution()
print(s.hammingWeight(11))  # 3
print(s.hammingWeight(128))  # 1
print(s.hammingWeight(2147483645))  # 30
