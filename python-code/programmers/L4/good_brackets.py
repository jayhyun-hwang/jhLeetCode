# https://school.programmers.co.kr/learn/courses/30/lessons/12929

import sys

sys.setrecursionlimit(10**6)

def find_good(text, open_count, close_count, answer_set):
    if open_count == 0 and close_count == 0:
        answer_set.add(text)
        return
    if open_count > close_count:
        return
    if open_count > 0:
        find_good(text + '(', open_count - 1, close_count, answer_set)
    if close_count > 0:
        find_good(text + ')', open_count, close_count - 1, answer_set)
    return


def solution(n):
    answer = 0
    a_set = set()
    find_good('', n, n, a_set)
    # print(a_set)
    answer = len(a_set)
    return answer


print(solution(2))
print(solution(3))
print(solution(10))
print(solution(13))
print(solution(15))
