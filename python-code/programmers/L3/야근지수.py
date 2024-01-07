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


# import heapq

def solution2(n, works):
    if sum(works) <= n:
        return 0
    
    max_heap = []
    for w in works:
        heapq.heappush(max_heap, -1 * w)
    
    remain = n
    while remain > 0:
        the_max = abs(heapq.heappop(max_heap))
        second_max = abs(heapq.heappop(max_heap))
        diff = the_max - second_max
        push_list = []
        if diff >= remain:
            push_list.append(the_max - remain)
            push_list.append(second_max)
            remain = 0
        else:
            if diff < 1:
                push_list.append(the_max - 1)
                push_list.append(second_max)
                remain -= 1
            else:
                push_list.append(the_max - diff)
                push_list.append(second_max)
                remain -= diff
        for ele in push_list:
            heapq.heappush(max_heap, -1 * ele)
    
    fatigue = 0
    for n in max_heap:
        fatigue += n ** 2
    return fatigue


print(solution(4, [4, 3, 3])) # 12
print(solution(1, [2, 1, 2])) # 6
print(solution(3, [1,1])) # 0

print(solution2(4, [4, 3, 3])) # 12
print(solution2(1, [2, 1, 2])) # 6
print(solution2(3, [1,1])) # 0
