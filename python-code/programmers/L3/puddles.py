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
    puddle_set = set()
    for p in puddles:
        puddle_set.add((p[1] - 1, p[0] - 1))
    map[0][0] = 1
    puddle_set.add((0, 0))
    for row_idx in range(n):
        for col_idx in range(m):
            if (row_idx, col_idx) in puddle_set:
                continue
            pre_col = map[row_idx][col_idx - 1] if col_idx > 0 else 0
            pre_row = map[row_idx - 1][col_idx] if row_idx > 0 else 0
            map[row_idx][col_idx] = (pre_col + pre_row) % 1000000007
    return map[-1][-1]


print(solution(4, 3, [[2, 2]]))  # 4
