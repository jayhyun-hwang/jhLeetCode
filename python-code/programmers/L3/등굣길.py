# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# dp == 점화식 == reduce 처럼 생각하자

# import sys

# sys.setrecursionlimit(10**6)

# def go_to_next(col, row, last_col, last_row, pud_set, res_list):
#     if col == last_col and row == last_row:
#         return res_list.append(True)
#     if col > last_col or row > last_row or (col, row) in pud_set:
#         return
#     go_to_next(col + 1, row, last_col, last_row, pud_set, res_list)
#     go_to_next(col, row + 1, last_col, last_row, pud_set, res_list)

# def solution(m, n, puddles):
#     answer = 0
#     puddle_set = set()
#     res_list = []
#     for ele in puddles:
#         puddle_set.add(tuple(ele))
#     go_to_next(1, 1, m, n, puddle_set, res_list)
#     count = len(res_list)
#     answer = count % 1000000007
#     return answer


def solution(m, n, puddles):
    map = [[0 for y in range(m)] for x in range(n)]
    puddles_set = set()
    for puddle in puddles:
        puddles_set.add((puddle[0] - 1, puddle[1] - 1))
    map[0][0] = 1
    puddles_set.add((0, 0))
    for row_idx in range(len(map)):
        for col_idx in range(len(map[0])):
            if (col_idx, row_idx) in puddles_set:
                continue
            left = 0 if col_idx == 0 else map[row_idx][col_idx - 1]
            upper = 0 if row_idx == 0 else map[row_idx - 1][col_idx]
            map[row_idx][col_idx] = left + upper
    return map[-1][-1] % 1000000007


print(solution(4, 3, [[2, 2]]))  # 4
