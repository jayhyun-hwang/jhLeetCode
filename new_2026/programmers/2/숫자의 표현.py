def solution(n):
    answer = 1  # 자기 자신
    if n == 1:
        return answer
    left, right = 0, 1
    tmp_sum = left + right

    while left + right <= n:
        if tmp_sum == n:
            answer += 1
            right += 1
            tmp_sum += right
            continue
        if tmp_sum < n:
            right += 1
            tmp_sum += right
            continue
        if tmp_sum > n:
            left += 1
            tmp_sum -= left

    return answer


print(solution(15))
print(solution(16))