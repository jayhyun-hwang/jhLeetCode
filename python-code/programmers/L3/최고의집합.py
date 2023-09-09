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


print(
    solution(13, 795463)
)  #	[61189, 61189, 61189, 61189, 61189, 61189, 61189, 61190, 61190, 61190, 61190, 61190, 61190]
print(
    solution2(13, 795463)
)  #	[61189, 61189, 61189, 61189, 61189, 61189, 61189, 61190, 61190, 61190, 61190, 61190, 61190]
