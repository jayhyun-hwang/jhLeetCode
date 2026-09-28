# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    route_map = [[0 for y in range(m)] for x in range(n)]

    for pud in puddles:
        x, y = pud
        route_map[y - 1][x - 1] = -1

    route_map[0][0] = 1
    for row_idx, row in enumerate(route_map):
        for col_idx, col in enumerate(row):
            if (row_idx == 0 and col_idx == 0) or route_map[row_idx][col_idx] == -1:
                continue
            left = 0
            if col_idx > 0:
                left = route_map[row_idx][col_idx - 1]
            if left == -1:
                left = 0

            upper = 0
            if row_idx > 0:
                upper = route_map[row_idx - 1][col_idx]
            if upper == -1:
                upper = 0

            route_map[row_idx][col_idx] = left + upper

    answer = route_map.pop().pop() % 1_000_000_007
    return answer
