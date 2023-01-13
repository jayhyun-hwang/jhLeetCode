import sys
from typing import List


def solution(stones: List[int], k: int) -> int:
    sys.setrecursionlimit(10 ** 9)
    answer = 0
    count = 0

    def pass_one(stones: List[int], count: int):
        term = 0
        print(stones)
        for idx, val in enumerate(stones):
            if val > 0:
                term = 0
                stones[idx] = val - 1
                continue
            term += 1
            if term >= k:
                return count
        count += 1
        return pass_one(stones, count)

    answer = pass_one(stones, count)
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))