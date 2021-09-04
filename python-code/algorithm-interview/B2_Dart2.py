# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    scoreIdx = 0
    scores = []
    temp = ''
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            scores.append(int(temp))
            temp = ''  
            scoreIdx += 1
        elif dartResult[i] == 'D':
            scores.append(int(temp))
            temp = ''  
            scoreIdx += 1
            scores[scoreIdx-1] **= 2
        elif dartResult[i] == 'T':
            scores.append(int(temp))
            temp = ''  
            scoreIdx += 1
            scores[scoreIdx-1] **= 3
        elif dartResult[i] == '*':
            scores[scoreIdx-1] *=2
            if scoreIdx > 1:
                scores[scoreIdx-2] *=2
        elif dartResult[i] == '#':
            scores[scoreIdx-1] *= -1
        else:
            temp += dartResult[i]
    answer = sum(scores)    # 배열의 합계 함수
    return answer

print(solution("1T2D3D#"))