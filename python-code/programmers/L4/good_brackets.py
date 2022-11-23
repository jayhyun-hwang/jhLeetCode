# https://school.programmers.co.kr/learn/courses/30/lessons/12929

import sys

sys.setrecursionlimit(10**6)
count = 0
def find_good(text, open_count, close_count):
    # print('open')
    # print(open_count)
    # print('close')
    # print(close_count)
    if open_count == 0 and close_count == 0:
        # answer_set.add(text)
        count += 1
        return
    if open_count > close_count:
        return
    if open_count < 0:
        find_good(text + '(', open_count - 1, close_count)
    if close_count < 0:
        find_good(text + ')', open_count, close_count - 1)

def solution(n):
    find_good('', n, n)
    return count
  
print(solution(2))
print(solution(3))