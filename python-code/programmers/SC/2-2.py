import collections
from typing import Collection, List


def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:

    time = 0
    truckQueue = collections.deque()
    timeQueue = collections.deque()
    total = 0
    for truck in truck_weights:
        if total + truck > weight:
            time += bridge_length
            total -= truckQueue.popleft()
        else:
            total += truck
            truckQueue.append(truck)
            time += 1

    return time

print(solution(2, 10, [7,4,5,6]))