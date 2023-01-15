import sys

sys.setrecursionlimit(10**6)


def solution(triangle):
    answer = 0
    res_list = [triangle[0]]
    for idx, list in enumerate(triangle):
        if idx == 0:
            continue
        tmp_list = []
        for val in list:
            tmp_list.append()

    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
