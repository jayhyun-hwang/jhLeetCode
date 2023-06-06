import heapq
import sys
from typing import List

sys.setrecursionlimit(10**9)


def solution(n: int, works: List[int]) -> int:
    answer = 0
    if sum(works) <= n:
        return 0
    if len(works) < 2:
        return (works.pop() - n)**2
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    while True:
        if n <= 0:
            break
        h1 = heapq.heappop(heap)
        h2 = heapq.heappop(heap)
        diff = abs(h1 - h2)
        if diff < 1:
            h1 += 1
            n -= 1
        else:
            if diff <= n:
                h1 += diff
                n -= diff
            else:
                h1 += n
                n = 0
        heapq.heappush(heap, h1)
        heapq.heappush(heap, h2)
    for val in heap:
        answer += val**2
    return answer