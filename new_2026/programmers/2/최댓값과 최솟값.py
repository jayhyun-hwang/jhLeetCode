def solution(s):
    num_list = s.split(" ")
    min_num = int(num_list[0])
    max_num = int(num_list[0])

    for val in num_list:
        tmp_num = int(val)
        if tmp_num < min_num:
            min_num = tmp_num
        if tmp_num > max_num:
            max_num = tmp_num

    return str(min_num) + " " + str(max_num)
