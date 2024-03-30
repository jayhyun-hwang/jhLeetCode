from typing import List


def solution(progresses, speeds):
    if len(progresses) == 1:
        return [1]
    answer = []
    days = 0
    q = (100 - progresses[0]) // speeds[0]
    r = (100 - progresses[0]) % speeds[0]
    if r > 0:
        q += 1
    days += q
    temp = 1
    progresses = progresses[1:]
    speeds = speeds[1:]
    for i, p in enumerate(progresses):
        progressed = p + (speeds[i] * days)
        if progressed >= 100:
            temp += 1
            continue
        answer.append(temp)
        temp = 0
        q = (100 - progressed) // speeds[i]
        r = (100 - progressed) % speeds[i]
        if r > 0:
            q += 1
        days += q
        temp += 1
    answer.append(temp)
    return answer


def solution2(progresses: List[int], speeds: List[int]) -> List[int]:
    answer = []
    # 배포가 끝날 때 까지
    while True:

        q, r = divmod(100 - progresses[0], speeds[0])
        if r > 0:
            q += 1

        for idx in range(len(progresses)):
            if progresses[idx] >= 100:
                continue
            progresses[idx] += speeds[idx] * q

        deployeeCount = 0
        for val in progresses:
            if val >= 100:
                deployeeCount += 1
            else:
                break
        answer.append(deployeeCount)
        if deployeeCount >= len(progresses):
            break
        progresses = progresses[deployeeCount:]
        speeds = speeds[deployeeCount:]

    return answer
