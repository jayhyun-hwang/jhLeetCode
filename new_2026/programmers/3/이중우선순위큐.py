# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq


def solution(operations):
    asc_heap = []
    desc_heap = []

    for val in operations:
        cmd, num_str = val.split(" ")
        num = int(num_str)
        if cmd == "I":
            heapq.heappush(asc_heap, (num, num))
            heapq.heappush(desc_heap, (-num, num))
        elif cmd == "D":
            if len(asc_heap) < 1:
                continue
            if num > 0:
                target_heap = desc_heap.copy()
            else:
                target_heap = asc_heap.copy()

            heapq.heappop(target_heap)

            desc_heap = []
            asc_heap = []
            for _, ele in target_heap:
                heapq.heappush(desc_heap, (-ele, ele))
                heapq.heappush(asc_heap, (ele, ele))

    if len(desc_heap) < 1:
        return [0, 0]

    answer = []
    answer.append(heapq.heappop(desc_heap)[1])
    answer.append(heapq.heappop(asc_heap)[1])
    return answer
