from typing import List
import heapq


def solution(scoville: List[int], K: int) -> int:
    if K < 1:
        return 0
    
    answer = 0

    # 오답. 브루트 포스. 정확성 O
    while True:
        scoville.sort()
        if scoville[0] >= K:
                break
        else:
            if len(scoville) == 1:
                return -1
            else:
                scoville[1] = scoville[0] + scoville[1] * 2
                scoville = scoville[1:]
                answer += 1
    return answer

print(solution([9, 10, 12, 1, 2, 3], 7))