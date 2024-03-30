import collections


def solution(cacheSize, cities):
    if cacheSize < 1:
        return len(cities) * 5
    cache_set = set()
    cache_q = collections.deque()
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache_set:
            time += 1
            cache_q.remove(city)
            cache_q.appendleft(city)
            continue
        time += 5
        if len(cache_q) >= cacheSize:
            cache_set.remove(cache_q.pop())
        cache_set.add(city)
        cache_q.appendleft(city)
    answer = time
    return answer


print(solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork",
      "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3,	["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 60
