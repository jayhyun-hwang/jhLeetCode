# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
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


print(
    solution(
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE",
         "DIA"]))  # 	[3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"]))  # 	[1, 3]
print(solution(["XYZ", "XYZ", "XYZ"]))  # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))  # [1, 5]
