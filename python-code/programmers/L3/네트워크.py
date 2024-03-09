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

# import sys

# sys.setrecursionlimit(10 ** 9)
def find_path(index, computer_list, visited):
    visited.add(index)
    cur = computer_list[index]
    for i, com in enumerate(cur):
        if com == 0 or i in visited:
            continue
        find_path(i, computer_list, visited)


def solution2(n, computers):
    if n == 1:
        return 1
    count = 0
    visited = set()
    for idx in range(n):
        if idx in visited:
            continue
        count += 1
        find_path(idx, computers, visited)
    return count

def solution3(n, computers):
    visited = set()
    count = 0
    for idx, com in enumerate(computers):
        if idx in visited:
            continue
        count += 1
        visited.add(idx)
        stack = []      
        for i, ele in enumerate(com):
            if ele == 1:
                stack.append(i)
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.add(vertex)
            for j, val in enumerate(computers[vertex]):
                if val == 1:
                    stack.append(j)
    return count

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution3(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
