# import sys


# sys.setrecursionlimit(10**6)
def solution(triangle):
    answer = 0
    for idx, row in enumerate(triangle):
        if idx == 0:
            continue
        for ri, _ in enumerate(row):
            if ri == 0:
                row[ri] += triangle[idx - 1][ri]
                continue
            if ri >= len(row) - 1:
                row[ri] += triangle[idx - 1][ri - 1]
                continue
            row[ri] += triangle[idx - 1][ri - 1] if triangle[idx - 1][
                ri - 1] > triangle[idx - 1][ri] else triangle[idx - 1][ri]
    answer = max(triangle.pop())
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
