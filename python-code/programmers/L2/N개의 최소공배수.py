def solution(arr):
    n_dict = dict()
    for ele in arr:
        num = ele
        t = 2
        temp_dict = dict()
        while True:
            if num == 1:
                break
            if num % t == 0:
                if t not in temp_dict:
                    temp_dict[t] = 0
                temp_dict[t] += 1
                num = num / t
            else:
                t += 1
        for k, v in temp_dict.items():
            if k not in n_dict:
                n_dict[k] = v
            else:
                n_dict[k] = max(n_dict[k], v)
    res = 1
    for k, v, in n_dict.items():
        res *= (k ** v)
    return res


print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))  # 6
