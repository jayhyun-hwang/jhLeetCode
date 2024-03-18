def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    res_list = [0] * n
    res_list[0] = 1
    res_list[1] = 2
    for i in range(2, n):
        res_list[i] = (res_list[i - 1] + res_list[i - 2]) % 1234567
    # print(res_list)
    return res_list[-1]


print(solution(4))  # 5
print(solution(3))  # 3
