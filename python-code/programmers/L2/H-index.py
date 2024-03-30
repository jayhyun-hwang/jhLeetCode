import heapq


def solution(citations):
    citations.sort(reverse=True)
    temp = 0
    for cnt, c in enumerate(citations, start=1):
        if cnt > c:
            return temp
        temp = min(cnt, c)
    return len(citations)


print(solution([3, 0, 6, 1, 5]))  # 3
