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


def find_target(word_list, visited):
    


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    for idx, val in enumerate(words):
        if is_one_diff(begin, val) != True:
            continue
        
        visited = set()
        find_target()
    return answer