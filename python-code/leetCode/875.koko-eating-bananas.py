#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

import heapq


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        if len(piles) == 1:
            q = piles[0] // h
            r = piles[0] % h
            if r > 0:
                q += 1
            return q

        heap = []
        for p in piles:
            heapq.heappush(heap, -p)
        cur_min = heap[0]
        count = h - len(piles)
        # print(cur_min, count)
        while count > 0:
            # print(heap)
            a = -heapq.heappop(heap)
            q = a // 2
            r = a % 2
            q = q + 1 if r > 0 else q
            heapq.heappush(heap, -q)
            cur_min = heap[0]
            count -= 1
        return -cur_min
