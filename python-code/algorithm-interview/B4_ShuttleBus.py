# https://programmers.co.kr/learn/courses/30/lessons/17678

# 마지막 버스를 구한다.
# 마지막 버스에 탈 사람들을 구한다 O(n)
# 마지막에 탈 사람 mm -= 1

from typing import List


def solution(n: int, t: int, m: int, timetable: List[str]):
    answer = ''
    timetable.sort()
    
    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))