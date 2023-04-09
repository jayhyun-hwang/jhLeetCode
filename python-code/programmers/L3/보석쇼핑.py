# https://school.programmers.co.kr/learn/courses/30/lessons/67258

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

import collections

def solution(gems):
    num = len(set(gems))
    ret = []

    left = 0
    counter = collections.Counter()
    for right in range(len(gems)):
        counter[gems[right]] += 1
        right += 1
        while len(counter) == num:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            ret.append([left, right])

    return sorted(ret, key = lambda x: (x[1]-x[0], x[0]))[0]

print(
    solution(
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE",
         "DIA"]))  # 	[3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"]))  # 	[1, 3]
print(solution(["XYZ", "XYZ", "XYZ"]))  # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))  # [1, 5]
