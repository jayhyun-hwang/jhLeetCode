# https://school.programmers.co.kr/learn/courses/30/lessons/12971#
# dp는 점화식 배열을 초시화시켜서 시작하는 것이 낫다
# dp1 = [0] * len(sticker)

def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)
    answer = 0
    # dp1 = [0] * len(sticker)
    # dp2 = [0] * len(sticker)
    # print(dp1)
    detach_first = sticker.copy()
    detach_second = sticker.copy()
    detach_first[1] = detach_first[0]
    detach_first[-1] = 0
    detach_second[0] = 0
    for idx, val in enumerate(detach_first):
        if idx < 2:
            continue
        detach_first[idx] = max(detach_first[idx - 1], detach_first[idx - 2] + val)
    for idx, val in enumerate(detach_second):
        if idx < 2:
            continue
        detach_second[idx] = max(detach_second[idx - 1], detach_second[idx - 2] + val)
    first_max = max(detach_first)
    second_max = max(detach_second)
    # print(detach_first)
    # print(detach_second)
    answer = max(first_max, second_max)
    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10])) # 36
print(solution([1, 3, 2, 5, 4])) # 8
