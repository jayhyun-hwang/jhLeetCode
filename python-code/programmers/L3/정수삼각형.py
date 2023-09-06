def solution(triangle):
    answer = 0
    for r_idx, row in enumerate(triangle):
        if r_idx < 1:
            continue
        for idx, _ in enumerate(row):
            left = triangle[r_idx - 1][idx - 1] if idx > 0 else 0
            right = triangle[r_idx - 1][idx] if idx < len(row) - 1 else 0
            bigger = left if left > right else right
            triangle[r_idx][idx] += bigger
    answer = max(triangle[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30

def solution2(triangle):
    if (len(triangle) <= 1):
        return triangle.pop()
    answer = 0
    for i, row in enumerate(triangle):
        if i < 1:
            continue
        for j, ele in enumerate(row):
            left = 0 if j < 1 else triangle[i - 1][j - 1]
            right = 0 if j >= len(row) - 1 else triangle[i - 1][j]
            triangle[i][j] += max(left, right)
    answer = max(triangle.pop())
    return answer
  
print(solution2([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30