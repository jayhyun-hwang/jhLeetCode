from typing import List


def solution(phone_book: List[str]) -> bool:
    answer = True

    dict1 = {}
    shortestLen = 20
    for val in phone_book:
        if len(val) < shortestLen:
            shortestLen = len(val)
        dict1[val] = True

    for val in phone_book:
        if len(val) == shortestLen:
            continue
        for i in range(shortestLen, len(val)):
            if val[:i] in dict1:
                return False
    return answer
