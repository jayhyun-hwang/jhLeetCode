from typing import List

def solution(sortedArray: List[int], findValue: int) -> int:
    if len(sortedArray) == 1:
        if sortedArray[0] == findValue:
            return 0
        else:
            return -1
    
    answer = 0
    
    end = len(sortedArray) - 1
    start = 0
    idx = 0

    while True:
        idx = (start + end) // 2
        target = sortedArray[idx]
        if findValue == target:
            answer = idx
            break
        elif target < findValue:
            start = idx
            if end - start < 2:
                if sortedArray[end] == findValue:
                    answer = end
                    break
                else:
                    return -1
        elif target > findValue:
            end = idx
            if end - start < 2:
                if sortedArray[start] == findValue:
                    answer == start
                    break
                else:
                    return -1
    return answer

# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 1))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 2))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 5))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 7))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 10))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 15))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 18))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 20))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 17))
# print(solution([1, 2, 5, 7, 10, 15, 18, 20], 0))
print(solution([1], 0))
print(solution([1], 1))
print(solution([1], 2))
print(solution([1,2], 0))
print(solution([1,2], 1))
print(solution([1,2], 2))
print(solution([1,2], 3))
print(solution([1,2,5], -14))
print(solution([1,2,5], 1))
print(solution([1,2,5], 2))
print(solution([1,2,5], 5))
print(solution([1,2,5], 4))
print(solution([1,2,5], 3))
print(solution([1,2,5], 6))