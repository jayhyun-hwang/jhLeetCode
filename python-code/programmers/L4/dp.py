# https://school.programmers.co.kr/learn/courses/30/lessons/42897

from typing import List

def find_sum(idx: int, cur_sum: int, m_list: List[int]) -> int:
    if idx >= len(m_list) - 2:
        return cur_sum + m_list[idx]
    
    cur_sum += m_list[idx]
    if idx == len(m_list) - 3:
        return find_sum(idx + 2, cur_sum, m_list)
    if m_list[idx + 2] >=
    
def solution(money: List[int]) -> int:
    answer = 0
    
    res1 = find_sum(0, 0, money)
    res2 = find_sum(1, 0, money)
    
    return answer