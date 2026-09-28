# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    A.sort()
    B.sort()
    # print(A, B)

    score = 0
    a_pointer = 0
    b_pointer = 0

    while True:
        if b_pointer >= len(B):
            break

        a_val = A[a_pointer]
        b_val = B[b_pointer]
        if a_val >= b_val:
            b_pointer += 1
            continue

        a_pointer += 1
        b_pointer += 1
        if a_val < b_val:
            score += 1

    answer = score
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([4, 4, 4, 4], [1, 2, 4, 5]))
print(solution([1, 1, 1, 1, 2], [1, 1, 1, 1, 2]))
print(solution([1, 1, 6, 6, 6, 6, 7, 7, 7], [4, 4, 5, 5, 7, 7, 7, 8, 8]))
print(solution([1, 1, 6, 6, 6, 6, 7, 8, 9], [4, 4, 5, 5, 7, 7, 7, 9, 9]))
