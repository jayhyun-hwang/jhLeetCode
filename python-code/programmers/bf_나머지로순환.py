from typing import List

def solution(answers: List[int]) -> List[int]:
    answer = []

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0,0,0]
    
    for idx, val in enumerate(answers):
        if val == s1[idx % 5]:
            score[0] +=1
        if val == s2[idx % 8]:
            score[1] += 1
        if val == s3[idx % 10]:
            score[2] += 1

    maxScore = max(score)

    for idx, val in enumerate(score):
        if val == maxScore:
            answer.append(idx+1)
    return answer