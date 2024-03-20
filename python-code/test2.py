import collections
def solution(S, C):
    # cur_str = S
    # for i, ele in enumerate(C):
    #     print(i, ele)
    #     cur_num = 0
    #     def get_list(cur_num, cur_str):
    #         if cur_num == ele:
    #           cur_str = cur_str[:cur_num] + "$" + cur_str[cur_num:]
    #           return cur_str
    #         if cur_str[cur_num] != "$":
    #             cur_num += 1
    #             return get_list(cur_num, cur_str)
    #     res = get_list(cur_num, cur_str)
    #     print(res)
    d = collections.deque()
    d.append(1)
    print(d)

            

            

        # for _, char in enumerate(cur_str):
        #     if cur_num == ele:
        #         cur_str = cur_str[:cur_num] + "$" + cur_str[cur_num:]
        #         break
        #     if char != "$":
        #         cur_num += 1
        # splited = cur_str.split("$")

print(solution("aabcddbc", [3, 5, 1, 4, 7]))  # 3
