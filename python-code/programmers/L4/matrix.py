# https://school.programmers.co.kr/learn/courses/30/lessons/118670

from typing import List
import sys

sys.setrecursionlimit(10**6)


def rotate_next(rc: List[List[int]], row: int, col: int, val):
    if row == 0 and col == 0:
        return rc
    next_val = rc[row][col]
    rc[row][col] = val

    if row == 0:
        if col == len(rc[0]) - 1:
            return rotate_next(rc, row + 1, col, next_val)
        return rotate_next(rc, row, col + 1, next_val)
    if row == len(rc) - 1:
        if col == 0:
            return rotate_next(rc, row - 1, col, next_val)
        return rotate_next(rc, row, col - 1, next_val)
    if col == 0:
        return rotate_next(rc, row - 1, col, next_val)
    return rotate_next(rc, row + 1, col, next_val)


def rotate(rc: List[List[int]]):
    last = rc[1][0]
    rc = rotate_next(rc, 0, 1, rc[0][0])
    rc[0][0] = last
    return rc


def shift_row(rc: List[List[int]]):
    last = rc.pop()
    return [last] + rc


def solution(rc: List[List[int]], operations: List[str]) -> List[List[int]]:
    for val in operations:
        if val == 'Rotate':
            rc = rotate(rc)
            continue
        if val == 'ShiftRow':
            rc = shift_row(rc)
            continue
    answer = rc
    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               ["Rotate", "ShiftRow"]))  # 	[[8, 9, 6], [4, 1, 2], [7, 5, 3]]
print(
    solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]) ==
    [[8, 9, 6], [4, 1, 2], [7, 5, 3]])

print(
    solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],
             ["Rotate", "ShiftRow", "ShiftRow"
              ]))  # 	[[8, 3, 3], [4, 9, 7], [3, 8, 6]]
print(
    solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],
             ["Rotate", "ShiftRow", "ShiftRow"]) == [[8, 3, 3], [4, 9, 7],
                                                     [3, 8, 6]])

print(
    solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
             ["ShiftRow", "Rotate", "ShiftRow", "Rotate"
              ]))  # [[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]]
print(
    solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
             ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]) ==
    [[1, 6, 7, 8], [5, 9, 10, 4], [2, 3, 12, 11]])
