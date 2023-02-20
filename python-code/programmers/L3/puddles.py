# https://school.programmers.co.kr/learn/courses/30/lessons/42898
import sys

sys.setrecursionlimit(10**6)


def go_to_next(col, row, last_col, last_row, pud_set, res_list):
    if col == last_col and row == last_row:
        return res_list.append(True)
    if col > last_col or row > last_row or (col, row) in pud_set:
        return
    go_to_next(col + 1, row, last_col, last_row, pud_set, res_list)
    go_to_next(col, row + 1, last_col, last_row, pud_set, res_list)


def solution(m, n, puddles):
    answer = 0
    puddle_set = set()
    res_list = []
    for ele in puddles:
        puddle_set.add(tuple(ele))
    go_to_next(1, 1, m, n, puddle_set, res_list)
    count = len(res_list)
    answer = count % 1000000007
    return answer


print(solution(4, 3, [[2, 2]]))  # 4
