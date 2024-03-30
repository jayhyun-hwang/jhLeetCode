import heapq
import collections

def solution(priorities, location):
    answer = 0
    heap = []
    queue = collections.deque()
    for idx, val in enumerate(priorities):
        heapq.heappush(heap, (-val, idx))
        queue.append((idx, val))
    i = 1
    while queue:
        # print(queue)
        # print(heap)
        cur_i, cur_p = queue.popleft()
        max_ele = heapq.heappop(heap)
        if abs(max_ele[0]) <= cur_p:
            if cur_i == location:
                break
            heap = []
            for j, v in queue:
                heapq.heappush(heap, (-v, j))
            i += 1
            continue
        heapq.heappush(heap, max_ele)
        queue.append((cur_i, cur_p))
    return i