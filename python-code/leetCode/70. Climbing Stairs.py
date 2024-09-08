class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        acc = [0] * n
        acc[0] = 1
        acc[1] = 2
        for idx in range(2, n):
            acc[idx] = acc[idx - 1] + acc[idx - 2]
        return acc[-1]

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
