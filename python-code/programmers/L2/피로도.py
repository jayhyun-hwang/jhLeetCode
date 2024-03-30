import itertools


def solution(k, dungeons):
    # dungeons.sort(key=lambda x: -x[0])
    p_list = itertools.permutations(dungeons, len(dungeons))
    # print(p_list)

    max_cnt = 0
    for ele in p_list:
        temp_k = k
        cnt = 0
        for min_p, p in ele:
            if min_p <= temp_k:
                temp_k -= p
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt
