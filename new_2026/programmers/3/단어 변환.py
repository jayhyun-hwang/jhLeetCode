# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    def is_one_diff(first, second):
        diff = 0
        for num in range(len(first)):
            if first[num] != second[num]:
                diff += 1
                if diff > 1:
                    break
        return (diff == 1)

    stack = [begin]
    route = []
    visited = set()

    candidate_list = []
    while stack:
        vertex = stack.pop()
        if vertex == target:
            candidate_list.append(len(route))
            continue

        route.append(vertex)
        for w in words:
            if w in visited or is_one_diff(vertex, w) is not True:
                continue

            stack.append(w)
        visited.add(vertex)

    answer = min(candidate_list) if candidate_list else 0
    return answer
