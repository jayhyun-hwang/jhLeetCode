import collections
from typing import List


def solution(cacheSize: int, cities: List[str]) -> int:
    if cacheSize < 1:
        return len(cities) * 5
    answer = 0
    cache = collections.deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer +=5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))