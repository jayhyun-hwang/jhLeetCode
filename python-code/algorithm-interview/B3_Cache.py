# https://programmers.co.kr/learn/courses/30/lessons/17680
from typing import List


def solution(cacheSize: int, cities: List[str]) -> int:
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        for cac in cache:
            if city == cac:
                answer += 1
                break
        

    return answer