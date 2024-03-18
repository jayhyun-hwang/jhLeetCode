import math


def solution(n, a, b):
    [left, right] = [a, b] if a < b else [b, a]
    r = 1
    while True:
        if left + 1 == right and right % 2 == 0:
            break
        left = math.ceil((left / 2))
        right = math.ceil((right / 2))
        r += 1
    return r


print(solution(8, 4, 7))  # 3
