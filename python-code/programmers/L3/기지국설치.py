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
    empty_length_list = []
    cursor = 1
    for s in stations:
        if cursor > n:
            break
        start = s - w
        end = s + w
        if cursor >= start:
            cursor = end + 1
            #continue
        # if cursor < start:
        else:
            range_start = cursor
            range_end = start
            range_length = range_end - range_start
            empty_length_list.append(range_length)
            cursor = end + 1
    if cursor <= n:
        empty_length_list.append(n + 1 - cursor)
    needed = 0
    w_range = 2 * w + 1
    for l in empty_length_list:
        (q, r) = divmod(l, w_range)
        needed += q
        if r > 0:
            needed += 1
    answer = needed
    return answer


print(solution(11, [4, 11], 1))  # 3
print(solution(
    16,
    [9],
    2,
))  # 3
