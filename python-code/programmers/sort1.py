from typing import List


def solution(numbers: List[int]) -> str:
    answer = ''
    # 한자리 + 소수점으로 변환
    for idx in range(len(numbers)):
        if numbers[idx] >= 10:
            numbers[idx] = str(numbers[idx])[0] + "." + str(numbers[idx])[1:]

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