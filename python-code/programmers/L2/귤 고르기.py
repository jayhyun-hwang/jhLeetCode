import heapq


def solution(k, tangerine):
    count_dict = dict()
    for ele in tangerine:
        if ele not in count_dict:
            count_dict[ele] = 0
        count_dict[ele] += 1
    heap = []
    for v in count_dict.values():
        heapq.heappush(heap, -v)
    count = 0
    while True:
        count += 1
        val = abs(heapq.heappop(heap))
        if val >= k:
            break
        k -= val
    return count


print(solution(6,	[1, 3, 2, 5, 4, 5, 2, 3]))  # 3
print(solution(4,	[1, 3, 2, 5, 4, 5, 2, 3]))  # 2
print(solution(2,	[1, 1, 1, 1, 2, 2, 2, 3]))  # 1
