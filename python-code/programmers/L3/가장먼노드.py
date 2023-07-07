import collections


def solution(n, edge):
    answer = 0
    if n <= 2:
        return 1
    # node_arr = [[0 for i in range(n + 1)] for j in range(n + 1)]
    # for i, j in edge:
    #    node_arr[i][j] = 1
    #    node_arr[j][i] = 1
    # for i in range(1, n + 1):
    distance_arr = [0 for i in range(n + 1)]
    node_map = dict()
    for i, j in edge:
        if i not in node_map:
            node_map[i] = []
        node_map[i].append(j)
        if j not in node_map:
            node_map[j] = []
        node_map[j].append(i)
    # print(node_map)
    queue = collections.deque()
    visited = set()
    queue.append(1)
    visited.add(1)
    v = 0
    while queue:
        v = queue.popleft()
        # print(v)
        for t in node_map[v]:
            if t in visited:
                continue
            if distance_arr[t] == 0:
                distance_arr[t] = distance_arr[v] + 1
            visited.add(t)
            queue.append(t)
    # print(distance_arr)
    max_dist = max(distance_arr)
    for val in distance_arr:
        if val == max_dist:
            answer += 1
    return answer


print(solution(6,
               [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
print(solution(6, [[1, 4], [4, 3], [1, 2]]))  # 1

print(solution(6,
               [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
print(
    solution(11,
             [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9],
              [5, 9], [5, 10], [6, 10], [6, 11]]))  # 4
print(solution(4, [[1, 2], [2, 3], [3, 4]]))  #1
print(solution(2, [[1, 2]]))  # 1
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 2
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]))  # 1
print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]))  # 3
print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]))  # 1
print(solution(4, [[4, 3], [1, 3], [2, 3]]))  # 2
