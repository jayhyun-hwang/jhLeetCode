import sys

sys.setrecursionlimit(10**6)


def is_one_diff(word, target):
    result = False
    diff = 0
    for i, e in enumerate(target):
        if word[i] != e:
            diff += 1
        if diff > 1:
            break
    if diff == 1:
        result = True
    return result


def find_target(org, target, word_list, visited, cur_count, count_list):
    if org == target:
        count_list.append(cur_count)
        return
    for idx, word in enumerate(word_list):
        if idx in visited or is_one_diff(org, word) == False:
            continue
        new_visited = visited.copy()
        new_visited.add(idx)
        find_target(word, target, word_list, new_visited, cur_count + 1,
                    count_list)
    return


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    count_list = []
    visited = set()
    find_target(begin, target, words, visited, 0, count_list)
    answer = min(count_list)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
