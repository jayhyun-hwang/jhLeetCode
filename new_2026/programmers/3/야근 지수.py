# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq


def solution(n, works):
    answer = 0

    heap = []
    for w in works:
        heapq.heappush(heap, (-w, w))
    # print(heap)

    temp = n

    while temp > 0:
        first = heapq.heappop(heap)[1]
        if first == 0:
            return answer
        second = heapq.heappop(heap)[1]
        diff = first - second
        if diff == 0:
            first -= 1
            temp -= 1
        elif diff > temp:
            first = first - temp
            temp = 0
        elif diff <= temp:
            first = first - diff
            temp -= diff

        heapq.heappush(heap, (-first, first))
        heapq.heappush(heap, (-second, second))

    for val in heap:
        answer += val[1] ** 2
    return answer


solution(4, [4, 3, 3])  # 12
