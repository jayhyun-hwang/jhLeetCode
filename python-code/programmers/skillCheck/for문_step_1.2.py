from typing import List


def solution(x: int, n: int) -> List[int]:
    answear = []
    for i in range(n):
        answear.append(i * x)
    return answear