from typing import List

# 큰 수부터 정렬

def solution(numbers: List[int]) -> str:
    answer = ''

    sorted = []
    for val in numbers:
        while True:
            if val < 10 and val >= 1:
                sorted.append(val)
                break
            else:
                val = round(val / 10, 3)

    sorted.sort(reverse=True)

    for val in sorted:
        answer += str(val)
    # print(sorted)
    return answer.replace(".","")


print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))
# print(solution([0,1,10,111,213,1000,999,888,999]))