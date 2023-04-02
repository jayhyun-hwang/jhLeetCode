import sys

sys.setrecursionlimit(10**9)


def is_match(t_id, pattern):
    l = len(t_id)
    if l != len(pattern):
        return False
    for i in range(l):
        if pattern[i] == '*':
            continue
        if t_id[i] != pattern[i]:
            return False
    return True


def make_res(m_list, depth_idx, res_set, res_list):
    if depth_idx >= len(m_list):
        res_list.append(res_set)
        return
    for ele in m_list[depth_idx]:
        if len(res_set) < 1:
            res_set = set()
        if ele in res_set:
            continue
        res_set.add(ele)
        make_res(m_list, depth_idx + 1, res_set, res_list)


def solution(user_id, banned_id):
    answer = 0

    match_list = []
    for idx, b in enumerate(banned_id):
        for val in user_id:
            if is_match(val, b):
                if idx >= len(match_list):
                    match_list.append([])
                match_list[idx].append(val)
    res_list = []
    make_res(match_list, 0, set(), res_list)
    print(res_list)
    answer = len(res_list)

    return answer


print(
    solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
             ["fr*d*", "abc1**"]))  # 2
print(
    solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
             ["*rodo", "*rodo", "******"]))  # 2
print(
    solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
             ["fr*d*", "*rodo", "******", "******"]))  # 3
