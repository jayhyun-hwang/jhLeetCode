from typing import List
import heapq


def solution(scoville: List[int], K: int) -> int:
    if K < 1:
        return 0
    
    answer = 0

    # 리스트를 힙으로(이진 min 힙)
    # heapq.heapify(scoville)
    heap = []
    for val in scoville:
        heapq.heappush(heap, val)
    print(heap)    

    # 
    while True:
        if heap[0] >= K:
                break
        else:
            if len(heap) == 1:
                return -1
            else:
                heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
                answer += 1
    return answer

print(solution([9, 10, 12, 1, 2, 3], 7))