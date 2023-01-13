import heapq
import sys
from typing import List


def solution(stones: List[int], k: int) -> int:
    sys.setrecursionlimit(10**9)
    answer = 0

    value_idx_dict = dict()
    for idx, val in enumerate(stones):
        if val not in value_idx_dict:
            value_idx_dict[val] = [idx]
            continue
        value_idx_dict[val].append(idx)
    print(value_idx_dict)
    print(min(value_idx_dict))
    del value_idx_dict[min(value_idx_dict)]
    print(min(value_idx_dict))
    print(value_idx_dict)
    value_idx_dict.pop(min(value_idx_dict))
    print(min(value_idx_dict))
    print(value_idx_dict)

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


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
