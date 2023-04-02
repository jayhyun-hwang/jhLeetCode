# https://school.programmers.co.kr/learn/courses/30/lessons/64064

# 1. is_match를 모든 target에 대해 한 번만 실행할 수 있는 지 고민(패턴에 매칭되는 단어들을 미리 listup 해둠)
# 2. 중복되는 결과값들을 하나의 결과로 취급한다면, 단순하게 최종 결과에 담을 때, 해당 set이 중복되는 지 O(n)으로 탐색하자 - set은 요소 집합의 값들이 같은 지 비교할 수 있다.
    # for r in res_list:
    #     if r == res_set:
    #         return
    # res_list.append(res_set)
    # return
# 3. set에서 요소 제거 시, key Error를 내지 않기 위해서는 set1.remove(val) 대신 set1.discard(val) 함수를 사용

import sys

sys.setrecursionlimit(10 ** 9)

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
        for r in res_list:
            if r == res_set:
                return
        res_list.append(res_set)
        return
    for ele in m_list[depth_idx]:
        if depth_idx < 1:
            res_set = set()
        if ele in res_set:
            continue
        new_set = res_set.copy()
        new_set.add(ele)
        make_res(m_list, depth_idx + 1, new_set, res_list)
        
            
            
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
