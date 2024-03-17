import sys

sys.setrecursionlimit(10 ** 9)


def _solution(n):  # brute force
    if n == 1:
        return 1
    res_list = [0, 1]
    for i in range(2, n + 1):
        half = res_list[i // 2]
        if i % 2 == 1:
            half += 1
        used = min(res_list[i - 1] + 1, half)
        res_list.append(used)
    return res_list[-1]


def getMin(num, count):
    if num == 1:
        return count
    if num % 2 == 1:
        count += 1
    res = getMin(num // 2, count)
    return res


def solution(n):
    answer = getMin(n, 1)
    return answer


print(solution(5))  # 2
print(solution(6))  # 2
print(solution(5000))  # 5
