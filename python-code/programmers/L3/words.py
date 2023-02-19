# https://school.programmers.co.kr/learn/courses/30/lessons/43163


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
        new_word_list = word_list[:idx] + word_list[idx + 1:]
        # BFS를 사용할 때는 연산행위가 미칠 영향을 정확히 생각해야 한다. 아니면 멱등성을 보장하도록 신경쓰는 것이 맘편하다
        # cur_count += 1 
        # 이렇게 쓰면 cur_count가 for문의 다음 순번에도 영향을 끼치므로 잘못된 로직이다.
        # new_cnt = cur_count + 1 또는 함수에 cur_count + 1 대입을 사용해야 한다.
        print(cur_word + " -> " + val + ": " + str(cur_count))
        print(new_word_list)
        min_num = find_target(new_word_list, val, target_word, cur_count + 1,
                              min_num)
    print('----------------------------')
    return min_num


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    min_num = len(words) + 1 # unreachable value로 최소값을 설정
    min_num = find_target(words, begin, target, 0, min_num)
    answer = min_num if min_num <= len(words) else answer # unreachable이 아니면 해당 값 return, 아니면 불가 값 return
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
