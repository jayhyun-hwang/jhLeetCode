def solution(n, s):
    q = s // n
    if q < 1:
        return [-1]
    r = s % n
    answer = [q] * (n - r) + [q + 1] * r
    return answer
  
print(solution(	13, 795463)) # 	[61189, 61189, 61189, 61189, 61189, 61189, 61189, 61190, 61190, 61190, 61190, 61190, 61190]
