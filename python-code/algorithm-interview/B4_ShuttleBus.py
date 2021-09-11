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


    result = busTime
    bi = 0
    mem = 0
    for val in convTime:
        if val <= busSchedule[bi] and mem < m:
            mem += 1
            if mem == m:
                bi += 1
                mem = 0
                if bi >= len(busSchedule):
                    result = val - 1
                    break
        else:
            bi += 1
            mem = 0
            while bi < len(busSchedule):
                if val <= busSchedule[bi]:
                    mem += 1
                    if mem == m:
                        bi += 1
                        mem = 0
                        if bi >= len(busSchedule):
                            result = val - 1
                            break
                        continue
                    cont = True
                    break
                bi += 1

    if bi <= len(busSchedule) - 1:
        if bi < len(busSchedule) - 1:
            result = busSchedule.pop()
        elif bi == len(busSchedule) - 2 and mem >= m:
            result 
    rh = str(result // 60).zfill(2)
    rm = str(result % 60).zfill(2)

    answer = rh + ":" + rm
    return answer

# print(solution(2,10,2,["09:10", "09:09", "08:00"]))
# print(solution(2,10,2,["09:10", "09:09", "08:00"]))
# print(solution(2,10,2,["09:10", "09:09", "08:00"]))
print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))