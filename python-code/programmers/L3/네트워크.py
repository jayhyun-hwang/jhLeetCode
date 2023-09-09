import sys

sys.setrecursionlimit(10**9)


def find_network(idx, computers, visited):
    for i, linked in enumerate(computers[idx]):
        if linked != 1 or i in visited:
            continue
        visited.add(i)
        find_network(i, computers, visited)


def solution(n, computers):
    if n == 1:
        return 1
    visited = set()
    network_count = 0
    for i in range(n):
        if i in visited:
            continue
        network_count += 1
        find_network(i, computers, visited)

    answer = network_count
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
