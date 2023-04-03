# def solution(S, C):
#     tmp_list = []
#     cur_str = S
#     tmp_list.append(cur_str)
#     for i, ele in enumerate(C):
#         cur_num = 0
#         for ele in tmp_list:

# print(solution("aabcddbc", [3, 5, 1, 4, 7]))  # 3

q, r = divmod(100, 27)
print(q, r)
(q, r) = divmod(100, 27)
print(q, r)
a = divmod(100, 27)
print(a)

set1 = set([1,2,3,4,5])
set2 = set([5,4,3,2,1])

if set1 == set2:
    print('true')
else:
    print('false')

if set1 is set2:
    print('true2')
else:
    print('false2')