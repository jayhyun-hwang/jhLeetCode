def solution(s):
    answer = ''
    num_str_list = s.split(' ')
    num_list = []
    for ns in num_str_list:
        num_list.append(int(ns))
    max_num = num_list[0]
    min_num = num_list[0]
    for n in num_list:
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n
    answer = str(min_num) + ' ' + str(max_num)
    return answer

print(solution("1 2 3 4")) # 기댓값 〉	"1 4"
print(solution("-1 -2 -3 -4")) # 기댓값 〉	"-4 -1"
print(solution("-1 -1")) # 기댓값 "-1 -1"
