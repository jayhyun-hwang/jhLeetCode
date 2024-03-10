def is_one_diff(org, tgt):
    diff_cnt = 0
    for i, ele in enumerate(org):
        if ele != tgt[i]:
            diff_cnt += 1
        if diff_cnt > 1:
            return False
    return (diff_cnt == 1)


def find_path(word, target, visited, cur_cnt, cnt_list, words):
    if word in visited:
        return
    if word == target:
        cnt_list.append(cur_cnt)
        return
    visited.add(word)
    for ele in words:
        if is_one_diff(word, ele) != True:
            continue
        find_path(ele, target, visited.copy(), cur_cnt + 1, cnt_list, words)


def solution(begin, target, words):
    if target not in words:
        return 0
    cnt_list = []
    for word in words:
        if is_one_diff(begin, word) != True:
            continue
        visited = set()
        find_path(word, target, visited, 1, cnt_list, words)

    answer = min(cnt_list) if len(cnt_list) > 0 else 0
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
