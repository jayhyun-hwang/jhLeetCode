# https://school.programmers.co.kr/learn/courses/30/lessons/42891


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    remain = k
    is_complete = False
    while True:
        if is_complete == True:
            break
        for idx, val in enumerate(food_times):
            if val > 0:
                remain -= 1
                if remain == -1:
                    answer = idx + 1
                    is_complete = True
                    break
                food_times[idx] = val - 1

    return answer


print(solution([3, 1, 2], 5))  # 1
