# https://school.programmers.co.kr/learn/courses/30/lessons/12979


# def solution(n, stations, w):
#     answer = 0
#     a_list = [0 for x in range(n)]
#     for s in stations:
#         idx = s - 1
#         for i in range(idx - w, idx + w + 1):
#             if i >= 0 and i < n:
#                 a_list[i] = 1
#     cur_idx = 0
#     add = 0
#     step = 2 * w + 1
#     while True:
#         if cur_idx > n - 1:
#             break
#         if a_list[cur_idx] > 0:
#             cur_idx += 1
#             continue
#         if a_list[cur_idx] < 1:
#             add += 1
#             cur_idx += step
#     answer = add
#     return answer
def solution(n, stations, w):
    answer = 0
    a_list = [0 for x in range(n)]
    for s in stations:
        idx = s - 1
        for i in range(idx - w, idx + w + 1):
            if i >= 0 and i < n:
                a_list[i] = idx + w + 1
    cur_idx = 0
    add = 0
    step = 2 * w + 1
    while True:
        if cur_idx > n - 1:
            break
        if a_list[cur_idx] > 0:
            cur_idx = a_list[cur_idx]
            continue
        if a_list[cur_idx] < 1:
            add += 1
            cur_idx += step
    answer = add
    return answer