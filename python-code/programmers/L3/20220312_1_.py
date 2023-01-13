import sys
sys.setrecursionlimit(10**6)

def dp(length, history):
    if length in history:
        return history[length]

    history[length] = (dp(length-2, history) + dp(length-1, history)) % 1000000007
    return history[length]

def solution(n):
    history = {-1 : 0, -2 : 0, 0 : 0, 1: 1, 2: 2}

    return dp(n, history)
print(solution(4))
print(solution(11))