from typing import List


def solution(n: int, left: int, right: int) -> List[int]:
    answer = []

    if n <= 1:
        return [1]
    for val in range(left, right+1):
        v1 = val // n
        v2 = val % n
        print([v1, v2])
        if v2 < v1:
            answer.append(v1+1)
        else:
            answer.append(v2+1)
    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))
print(solution(3, 3, 3))
print(solution(3, 0, 0))
print(solution(1, 0, 0))
print(solution(1, 1, 1))