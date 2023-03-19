def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    b_idx = 0
    for a in A:
        if b_idx >= len(B):
            break
        while True:
            if b_idx >= len(B):
                break
            if B[b_idx] > a:
                answer += 1
                b_idx += 1
                break
            b_idx += 1
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))  # 3
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))  # 0
