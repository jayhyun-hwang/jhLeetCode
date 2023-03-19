# https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    camera = -30001
    start = 0
    end = 0
    for ele in routes:
        start = ele[0]
        end = ele[1]
        if start > camera:
            answer += 1
            camera = end
            continue
        camera = end if end < camera else camera
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
