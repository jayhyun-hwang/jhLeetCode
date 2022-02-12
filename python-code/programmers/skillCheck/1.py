from typing import List


def solution(n: int, left: int, right: int) -> List[int]:
    answer = []
    tempArr = []
    for i in range(n):
        rowArr = []
        for j in range(n):
            if j < i + 1:
                rowArr.append(i + 1)
            else:
                rowArr.append(j + 1)
        tempArr.append(rowArr)
    answer = tempArr
    return answer

def solution2(n: int, left: int, right: int) -> List[int]:
    answer = []
    for i in range(n):
        for j in range(n):
            if j < i + 1:
                answer.append(i + 1)
            else:
                answer.append(j + 1)
    print(answer)
    return answer[left:right+1]


print(solution2(3, 2, 5))
print(solution2(4, 7, 14))