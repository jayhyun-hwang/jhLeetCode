import heapq
import sys
from typing import List

def solution(n: int, works: List[int]) -> int:
    sys.setrecursionlimit(10 ** 9)
    answer = 0

    # 길이가 1일 때
    if len(works) == 1:
        temp_res = works[0] - n
        if temp_res < 0:
            return 0
        return temp_res ** 2
    
    heap = []
    for val in works:
        heapq.heappush(heap, -val)
    print(heap)
    def find_work_heap_result(time_n, work_heap):
        if time_n <= 0:
            return work_heap
        smallest = heapq.heappop(work_heap)
        if smallest == 0:
            return [0]
        smallest2 = work_heap[0]
        diff = smallest - smallest2

        if diff == 0:
            heapq.heappush(work_heap, smallest + 1)
            time_n -= 1
        elif time_n >= abs(diff): # 남은 time이 더 큰 경우, diff만큼만 뺌
            heapq.heappush(work_heap, smallest - diff)
            time_n += diff
        else:   # 남은 time이 더 작은 경우, 남은 시간만큼 뺌
            heapq.heappush(work_heap, smallest + time_n)
            time_n = 0
        return find_work_heap_result(time_n, work_heap)
    
    
    res_heap = find_work_heap_result(n, heap)
    for ele in res_heap:
        answer += ele ** 2
    return answer
# import heapq


# def solution(n, works):
#     answer = 0
#     total_works = sum(works)
#     if total_works <= n:
#         return answer
#     heapq.
#     while(True):
#         break    
#     return answer