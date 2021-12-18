from typing import List

# int to str. 오름차순 또는 내림차순으로 문자열로 이어붙여서 리스트 만들기

def solution(startNumber: int, endNumber: int) -> List[str]:
    answer = []

    temp = startNumber
    while True:
        answer.append(str(temp).zfill(10))
        if startNumber == endNumber:
            break
        
        if startNumber < endNumber:
            startNumber += 1
            temp = temp *10 + startNumber
        elif startNumber > endNumber:
            startNumber -= 1
            temp = temp *10 + startNumber
    return answer

print(solution(1,9))
print(solution(9,1))
print(solution(2,7))
print(solution(7,2))
print(solution(7,7))
