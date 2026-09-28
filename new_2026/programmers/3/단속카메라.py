# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    sorted_list = sorted(routes, key=lambda x: x[1])

    count = 1
    location = sorted_list[0][1]
    for start, end in sorted_list:
        if start <= location:
            continue

        count += 1
        location = end
    answer = count
    return answer
