# https://school.programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, [food_times[i], i])
    print(h)
    

    return answer


print(solution([3, 1, 2], 5))  # 1
