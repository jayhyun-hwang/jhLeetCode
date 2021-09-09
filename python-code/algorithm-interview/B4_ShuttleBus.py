# https://programmers.co.kr/learn/courses/30/lessons/17678

# 마지막 버스를 구한다.
# 마지막 버스에 탈 사람들을 구한다 O(n)
# 마지막에 탈 사람 mm -= 1

from typing import List


def solution(n: int, t: int, m: int, timetable: List[str]):
    answer = ''
    convTime = []
    
    for time in timetable:
        hhmm = time.split(":")
        hh = int(hhmm[0]) * 60
        mm = int(hhmm[1])
        convTime.append(hh+mm)
    
    convTime.sort()
    
    busTime = 540

    busSchedule = []
    for i in range(n):
        busSchedule.append(busTime + (t * i))

    print(busSchedule)
    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))