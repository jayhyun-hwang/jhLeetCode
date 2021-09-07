# https://programmers.co.kr/learn/courses/30/lessons/17680
from typing import List


def solution(cacheSize: int, cities: List[str]) -> int:
    if cacheSize < 1:
        return 5 * len(cities)
    answer = 0
    cache = []
    isin = False
    for city in cities:
        isin = False
        city = city.lower()
        for cac in cache:
            if city == cac:
                answer += 1
                cache.remove(cac)
                cache.append(city)
                isin = True
                break
        if isin:
            continue
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                del cache[0]
                cache.append(city)
    return answer

print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))