import sys


def solution(n: int) -> int:
    sys.setrecursionlimit(1500000)
    answer = 0
    count = 0
    def nextBlock(remLen: int):
        nonlocal count
        if remLen < 2:
            count += 1
            return
        nextBlock(remLen - 1)
        nextBlock(remLen - 2)
    nextBlock(n)
    answer = count % 1000000007
    return answer


print(solution(4))
print(solution(7))
print(solution(100))
# print(solution(60000))