from typing import List


def solution(numbers: List[int]) -> str:
    answer = ''
    # 한자리 + 소수점으로 변환
    for idx in range(len(numbers)):
        if numbers[idx] == 0:
            continue
        while True:
# 소수점 연산이 틀어져서 오답
            if numbers[idx] < 10 and numbers[idx] >= 1:
                break
            numbers[idx] /= 10
    # 정렬
    numbers.sort(reverse=True)
    # 합치기
    for val in numbers:
        answer += str(val)
    # . 없애기
    answer = answer.replace(".","")
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,1,10,111,213,1000,999,888,999]))