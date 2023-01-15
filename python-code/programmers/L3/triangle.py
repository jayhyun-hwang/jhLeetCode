import sys

sys.setrecursionlimit(10**6)


def add_sum(list, last_depth: int, depth_idx: int, row_idx: int, cur_sum: int,
            sum_list: list[int]):
    cur_sum += list[depth_idx][row_idx]
    print(cur_sum)
    if depth_idx >= last_depth:
        if len(sum_list) > 0:
            n = sum_list.pop()
            if n < cur_sum:
                n = cur_sum
            return sum_list.append(n)
        return sum_list.append(cur_sum)
    add_sum(list, last_depth, depth_idx + 1, row_idx, cur_sum, sum_list)
    return add_sum(list, last_depth, depth_idx + 1, row_idx + 1, cur_sum,
                   sum_list)


def solution(triangle: list[list[int]]):
    answer = 0
    sum_list = []
    add_sum(triangle, len(triangle) - 1, 0, 0, 0, sum_list)
    print(sum_list)
    answer = sum_list.pop()
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30