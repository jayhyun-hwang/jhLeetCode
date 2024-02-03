def solution(n):
    bin_str = bin(n)
    # print(bin_str)
    one_cnt = 0
    for ele in bin_str[2:]:
        if ele == '1':
            one_cnt += 1
    temp_num = n
    while True:
        temp_num += 1
        temp_cnt = 0
        for ele in bin(temp_num)[2:]:
            if ele == '1':
                temp_cnt += 1
        if temp_cnt == one_cnt:
            return temp_num