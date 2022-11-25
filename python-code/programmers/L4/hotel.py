# https://school.programmers.co.kr/learn/courses/30/lessons/64063
from typing import List
import sys

sys.setrecursionlimit(10**6)


def get_room(org_num: int, cur_num_list: List[int], res_dict):
    cur = cur_num_list[-1]
    if cur not in res_dict:
        for ele in cur_num_list:
            res_dict[ele] = cur + 1
        return cur
    cur_num_list.append(res_dict[cur])
    return get_room(org_num, cur_num_list, res_dict)


def solution(k: int, room_number: List[int]) -> List[int]:
    answer = []
    RES_DICT = dict()
    for val in room_number:
        answer.append(get_room(val, [val], RES_DICT))
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))  # [1,3,4,2,5,6]
