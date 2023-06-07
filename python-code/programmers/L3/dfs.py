import sys

sys.setrecursionlimit(10 ** 6)


def find_network(data_list, idx, visited):
    for i, val in enumerate(data_list[idx]):
        if i in visited:
            continue
        if val == 1:
            visited.add(i)
            find_network(data_list, i, visited)


def solution(n, computers):
    answer = 0
    completed = set()
    network = 0
    for idx, com in enumerate(computers):
        if idx in completed:
            continue
        network += 1
        find_network(computers, idx, completed)
    answer = network
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
