from typing import List

def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    answer = []
    # 배포가 끝날 때 까지
    while True:
        
        q, r = divmod(100 - progresses[0], speeds[0]) 
        if r > 0:
            q+=1
        
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

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))
print(solution([93, 30, 55], [1, 30, 5]))