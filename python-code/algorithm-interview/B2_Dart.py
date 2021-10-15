# https://programmers.co.kr/learn/courses/30/lessons/17682

from typing import List


def solution(dartResult):
    answer = 0
    scoreIdx = 0
    scores = ["","",""]
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            scores[scoreIdx] = int(scores[scoreIdx])
            scoreIdx += 1
        elif dartResult[i] == 'D':
            scores[scoreIdx] = int(scores[scoreIdx])
            scoreIdx += 1
            scores[scoreIdx-1] **= 2
        elif dartResult[i] == 'T':
            scores[scoreIdx] = int(scores[scoreIdx])
            scoreIdx += 1
            scores[scoreIdx-1] **= 3
        elif dartResult[i] == '*':
            scores[scoreIdx-1] *=2
            if scoreIdx - 2 > -1:
                scores[scoreIdx-2] *=2
        elif dartResult[i] == '#':
            scores[scoreIdx-1] *= -1
        else:
            scores[scoreIdx] += dartResult[i]
    for n in scores:
        answer += n
    return answer

print(solution("1T2D3D#"))