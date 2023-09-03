import sys

sys.setrecursionlimit = 10 ** 11

def move_to(n, from_poll, to_poll, sub_poll, process_list):
    if (n == 1):
        return process_list.append([from_poll, to_poll])
    move_to(n - 1, from_poll, sub_poll, to_poll, process_list)
    process_list.append([from_poll, to_poll])
    move_to(n - 1, sub_poll, to_poll, from_poll, process_list)

def solution(n):
    answer = []
    move_to(n, 1, 3, 2, answer)
    return answer

print(solution(24))