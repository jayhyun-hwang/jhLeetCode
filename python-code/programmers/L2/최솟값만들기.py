def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    last_idx = len(A) - 1
    for i in range(len(A)):
        answer += A[i] * B[last_idx - i]
    return answer


print(solution([1, 4, 2], [5, 4, 4]))  # 29
print(solution([1, 2], [3, 4]))  # 10
