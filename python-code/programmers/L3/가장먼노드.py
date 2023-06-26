import sys


sys.setrecursionlimit(10**6)

def solution(n, edge):
    answer = 0
    if n <= 2:
        return 1
    node_arr = [[0 for i in range(n + 1)] for j in range(n + 1)]
    distance_arr = [-1 for i in range(n + 1)]
    for i, j in edge:
        node_arr[i][j] = 1
        node_arr[j][i] = 1
    # print(node_arr)
    def find_distance(cur, end, dist, visited):
        # print(cur, end, dist, visited)
        if cur == end:
            if distance_arr[end] < 0:
                distance_arr[end] = dist
            else:
                distance_arr[end] = min(distance_arr[end], dist)
            return
        visited.add(cur)
        if node_arr[cur][end] == 1:
            return find_distance(end, end, dist + 1, visited)
        for idx, next_node in enumerate(node_arr[cur]):
            if idx < 1 or next_node < 1 or idx in visited:
                continue
            v = set()
            v.add(cur)
            find_distance(idx, end, dist + 1, v)
    
    for i in range(1, n + 1):
        print(i)
        find_distance(1, i, 0, set())
    print(distance_arr)
    max_dist = max(distance_arr)
    for val in distance_arr:
        if val == max_dist:
            answer += 1
    return answer


# print(solution(6,
#                [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
# print(solution(6, [[1, 4], [4, 3], [1, 2]]))  # 1

# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]])) # 4
# print(solution(4, [[1, 2], [2, 3], [3, 4]])) #1
# print(solution(2, [[1, 2]])) # 1
# print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 2
# print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]])) # 1
# print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]])) # 3
# print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]])) # 1
# print(solution(4, [[4, 3], [1, 3], [2, 3]])) # 2