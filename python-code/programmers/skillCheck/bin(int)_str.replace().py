from typing import List

# 문자열을 이진수로 바꾸고 0 지우기
def solution(s: str) -> List[int]:
    answer = [0,0]

    while True:
        if len(s) == 1:
            break
        for val in s:
            if val == "0":
                answer[1] += 1
        s = s.replace("0","")
        s = bin(len(s))[2:]
        answer[0] += 1

    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

