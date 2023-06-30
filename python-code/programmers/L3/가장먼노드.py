import sys


sys.setrecursionlimit(10**6)

INF = int(1e9)
def solution(n, edge):
    answer = 0
    if n <= 2:
        return 1
    node_arr = [[0 for i in range(n + 1)] for j in range(n + 1)]
    distance_arr = [INF for i in range(n + 1)]
    for i, j in edge:
        node_arr[i][j] = 1
        node_arr[j][i] = 1
    print(node_arr)
    visited = set()
    for i in range(1, n + 1):
        visited.add(i)
        for j in range(1, n + 1):
            if node_arr[i][j] == 1:

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