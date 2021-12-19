import heapq
from typing import List


def solution(n:int, times: List[int]) -> int:
    answer = 0

    heapq.heapify(times)
    for i in range(n):
      heapq.heappush(times, heapq.heappop(times))  

    return answer

print(solution(6, [10, 7]))