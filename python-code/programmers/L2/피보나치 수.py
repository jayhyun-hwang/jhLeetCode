def solution(n):
    answer = 0
    if n == 2:
        return 1
    fb = [0, 1]
    for i in range(2, n + 1):
        temp = fb[i - 2] + fb[i - 1]
        fb.append(temp)
    answer = fb[-1] % 1234567

    return answer


print(solution(3)) # 2
print(solution(5)) # 5
