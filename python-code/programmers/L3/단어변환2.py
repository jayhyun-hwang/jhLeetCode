def is_one_diff(org, tgt):
    diff_count = 0
    for i in range(len(org)):
        if org[i] != tgt[i]:
            diff_count += 1
        if diff_count > 1:
            break
    return (diff_count == 1)

def find_dfs(v, tgt_word, pre_word, cur_word, word_list, cl):
    if cur_word in v or is_one_diff(pre_word, cur_word) == False:
        return
    if cur_word == tgt_word:
        cl.append(len(v) + 1)
        return
    v.add(cur_word)
    for w in word_list:
        find_dfs(v.copy(), tgt_word, cur_word, w, word_list, cl)

def solution(begin, target, words):
    answer = 0
    complete_list = []
    if target not in words:
        return answer
    for word in words:
        visited = set()
        find_dfs(visited, target, begin, word, words, complete_list)
    answer = 0 if len(complete_list) == 0 else min(complete_list)
    print(complete_list)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
