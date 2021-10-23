from typing import List


def solution(sortedArray: List[int], findValue: int) -> int:
    answer = 0

    searchArr = sortedArray
    idx = len(searchArr) // 2
    while True:
        target = searchArr[idx]
        if findValue == target:
            answer = idx
            break
        elif findValue < target:
            searchArr = searchArr[:idx]
        elif findValue > target:
            searchArr = searchArr[idx:]
        
        


    return answer

print(solution([1, 2, 5, 7, 10, 15, 18, 20], 15))
print(solution([1, 2, 5, 7, 10, 15, 18, 20], 17))