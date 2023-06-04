# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if s < n:
        return [-1]
    q = s // n
    r = s % n
    return [q] * (n - r) + [q + 1] * r
  
print(solution(13, 795463)) #	[61189, 61189, 61189, 61189, 61189, 61189, 61189, 61190, 61190, 61190, 61190, 61190, 61190]