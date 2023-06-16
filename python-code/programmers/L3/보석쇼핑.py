# https://school.programmers.co.kr/learn/courses/30/lessons/67258


# 정확성만
def solution2(gems):
    answer = []
    gems_set = set()
    gems_length = len(gems)
    for g in gems:
        gems_set.add(g)
    # print(gems_set)
    res = [gems_length - 1, [0, gems_length - 1]]
    for i in range(gems_length):
        tmp_set = gems_set.copy()
        for idx in range(i, gems_length):
            if idx - i > res[0]:
                continue
            if gems[idx] in tmp_set:
                tmp_set.discard(gems[idx])
            if len(tmp_set) < 1:
                if idx - i < res[0]:
                    res = [idx - i, [i, idx]]
                    break
    answer = [res[1][0] + 1, res[1][1] + 1]
    return answer


# import collections

# def solution(gems):
#     num = len(set(gems))
#     ret = []

#     left = 0
#     counter = collections.Counter()
#     for right in range(len(gems)):
#         counter[gems[right]] += 1
#         right += 1
#         while len(counter) == num:
#             counter[gems[left]] -= 1
#             if counter[gems[left]] == 0:
#                 del counter[gems[left]]
#             left += 1
#             ret.append([left, right])

#     return sorted(ret, key = lambda x: (x[1]-x[0], x[0]))[0]


def solution(gems):
    answer = []
    satisfied_num = len(set(gems))
    if satisfied_num == 1:
        return [1, 1]
    min_num = len(gems) + 1
    left, right = 0, 0
    gem_dict = dict()
    gem_dict[gems[left]] = 1
    move_right = True
    while True:
        if right != 0 and left == right:
            break
        if move_right:
            if right >= len(gems) - 1:
                break
            right += 1
            if gems[right] in gem_dict:
                gem_dict[gems[right]] += 1
            else:
                gem_dict[gems[right]] = 1
        else:
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
            left += 1
        if len(gem_dict) == satisfied_num:
            if right - left < min_num:
                min_num = right - left
                answer = [left + 1, right + 1]
            move_right = False
        else:
            move_right = True

    return answer


print(
    solution(
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE",
         "DIA"]))  # 	[3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"]))  # 	[1, 3]
print(solution(["XYZ", "XYZ", "XYZ"]))  # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))  # [1, 5]

print(solution(["A", "A", "A", "B", "B"]))  # 3, 4
print(solution(["A"]))  # 1, 1
print(solution(["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]))  # 8, 10
print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D",
                "B"]))  # 3, 7