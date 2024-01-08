# https://school.programmers.co.kr/learn/courses/30/lessons/12938


def solution(n, s):
    if s < n:
        return [-1]
    q = s // n
    r = s % n
    return [q] * (n - r) + [q + 1] * r


def solution2(n, s):
    if n > s:
        return [-1]
    val = s // n
    rem = s % n
    result = []
    for _ in range(n):
        result.append(val)
    for i in range(rem):
        idx = n - i - 1
        result[idx] += 1
    return result

def solution3(n, s):
    if n > s:
        return [-1]
    answer = []
    q = s // n
    r = s % n
    for _ in range(n - r):
        answer.append(q)
    for _ in range(r):
        answer.append(q + 1)
    return answer


print(
    solution(13, 795463)
)  #	[61189, 61189, 61189, 61189, 61189, 61189, 61189, 61190, 61190, 61190, 61190, 61190, 61190]
print(
    solution2(13, 795463)
)  #	[61189, 61189, 61189, 61189, 61189, 61189, 61189, 61190, 61190, 61190, 61190, 61190, 61190]
print(
    solution3(13, 795463)
)  #	[61189, 61189, 61189, 61189, 61189, 61189, 61189, 61190, 61190, 61190, 61190, 61190, 61190]
