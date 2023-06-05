import sys

sys.setrecursionlimit(10**6)


def find_network(idx, computers, visited):
    for i, val in enumerate(computers[idx]):
        if val == 0 or i in visited:
            continue
        visited.add(i)
        find_network(i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = set()
    network_count = 0
    for i, com in enumerate(computers):
        if i in visited:
            continue
        network_count += 1
        find_network(i, computers, visited)
    answer = network_count
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
