import collections
from typing import List


def solution(priorities: List[int], location: int) -> int:
    answer = 0

    priStack = collections.deque([i for i in range(len(priorities))])
    priDict = dict()
    for idx, val in enumerate(priorities):
        priDict[idx] = val
    print(priDict)
    print(priStack)

    outOrder = 1
    while True:
        nowIdx = priStack.popleft()
        isOut = True
        for curIdx in priStack:
            if priDict[nowIdx] < priDict[curIdx]:
                priStack.append(nowIdx)
                isOut = False
                break
        if isOut == True:
            if nowIdx == location:
                answer = outOrder
                break
            outOrder += 1

    return answer


print(
    "anwser = ",
    solution([2, 1, 3, 2, 2, 1, 3, 4, 5, 6, 8, 5, 4, 2, 2, 4, 6, 8, 7, 5, 4],
             2))
