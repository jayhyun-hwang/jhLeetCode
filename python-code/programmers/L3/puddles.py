# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# dp == 점화식 == reduce 처럼 생각하자

import sys

sys.setrecursionlimit(10**6)


def go_to_next(col, row, last_col, last_row, pud_set, res_list):
    if col == last_col and row == last_row:
        return res_list.append(True)
    if col > last_col or row > last_row or (col, row) in pud_set:
        return
    go_to_next(col + 1, row, last_col, last_row, pud_set, res_list)
    go_to_next(col, row + 1, last_col, last_row, pud_set, res_list)


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
    print(map)
    puddle_set = set()
    for p in puddles:
        puddle_set.add((p[0], p[1]))
    print(puddle_set)
    map[0][0] = 1
    puddle_set.add((0,0))
    print(map)
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if (row_idx, col_idx) in puddles:
                continue
            pre_col = map[row_idx][col_idx - 1] % 1000000007 if col_idx > 0 else 0
            pre_row = map[row_idx - 1][col_idx] % 1000000007 if row_idx > 0 else 0
            print(pre_col)
            map[row_idx][col_idx] = pre_col + pre_row % 1000000007
    print(map)
    return map.pop().pop()

print(solution(4, 3, [[2, 2]]))  # 4


# answer
def solution2(m, n, puddles):  #m는열 n는 행
    map = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    map[1][1] = 1
    print('--------------------')
    print(map)
    print('--------------------')
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:
                continue
            # if [y,x] in puddles:
            #     map[x][y] =0
            if y == puddles[0][1] and x == puddles[0][0]:  # 웅덩이 위치의 경우 값을 0으로
                map[x][y] = 0
            else:
                map[x][y] = (map[x - 1][y] + map[x][y - 1]) % 1000000007
    print(map)
    return map[n][m]


# print(solution2(4, 3, [[2, 2]]))  # 4
