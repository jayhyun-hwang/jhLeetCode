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


def find_target(word_list, cur_word, target_word, cur_count, min_num):
    if cur_word == target_word:
        return cur_count if cur_count < min_num else min_num
    for idx, val in enumerate(word_list):
        if is_one_diff(cur_word, val) == False:
            continue
        print(word_list)
        print(word_list[idx])
        new_word_list = word_list.copy()
        del new_word_list[idx]
        min_num = find_target(new_word_list, val, target_word, cur_count + 1,
                              min_num)
    return min_num


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    min_num = len(words) + 1
    min_num = find_target(words, begin, target, 0, min_num)
    answer = min_num if min_num <= len(words) else answer
    return answer