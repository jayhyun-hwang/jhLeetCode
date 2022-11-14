# 나란히 늘어선 건물들의 높이를 왼쪽부터 차례대로 담고 있는 정부 배열 heights. 각 건물에서 보이는 자신보다 크거나 같은 건물들의 수를 모두 합한 값을 return
from typing import List


def get_building_count_forward(heights: List[int]) -> int:
    answer = 0
    visible_list_cache = dict()
    for i in range(1, len(heights)):
        print(heights[-i:])
        tp = tuple(heights[-i:])
        max_num = 0
        list = []
        for val in tp:
            if val > max_num:
                list.append(val)
                max_num = val
        visible_list_cache[tp] = list
    for i, val in enumerate(heights):
        building_list = heights[i + 1:]
        if len(building_list) < 1:
            break
        # print(building_list)
        count = 0
        vl = visible_list_cache[tuple(building_list)]
        for target in vl:
            if target >= val:
                count += 1
        answer += count
    return answer


def solution(heights: List[int]) -> int:
    answer = 0
    # print('--------------------------------')
    # print(heights)
    # print('--------------------------------')
    answer += get_building_count_forward(heights)
    # print('--------------------------------')
    # print(heights[::-1])
    # print('--------------------------------')
    answer += get_building_count_forward(heights[::-1])

    return answer


print(solution([1, 4, 2, 5, 3]))  # 6
# print(solution([3, 4, 5, 6, 7]))  # 10
# print(solution([5, 5, 5]))  # 4
# print(solution([1, 99998, 99999]))  # 3
# print(solution([3, 5, 4, 2, 4, 4, 6, 5]))  # 18
