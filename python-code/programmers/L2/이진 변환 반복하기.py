def solution(s):
    answer = []
    removed_cnt = 0
    value = s
    conv_cnt = 0
    while value != '1':
        temp_length = 0
        conv_cnt += 1
        for ele in value:
            if ele == '0':
                removed_cnt += 1
            else:
                temp_length += 1
        value = str(bin(temp_length)[2:])
        # print(bin(temp_length))
    answer.append(conv_cnt)
    answer.append(removed_cnt)
    return answer

    
# "110010101001"	[3,8]
# "01110"	[3,3]
# "1111111"	[4,1]
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
