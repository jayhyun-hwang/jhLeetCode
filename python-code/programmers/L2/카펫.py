def solution(brown, yellow):
    answer = []
    width = yellow + 1
    height = 1
    while width > 0:
        width -= 1
        if yellow % width != 0:
            continue
        height = yellow // width
        if brown == (width * 2) + (height * 2) + 4:
            answer = [width + 2, height + 2]
            break
    return answer

# 2차 방정식 풀이


def solution2(brown, yellow):
    answer = []
    a, b, c = 1, (2 - brown / 2), yellow
    d = (b ** 2) - (4*a*c)
    if d == 0:
        w1 = yellow ** 0.5
        w2 = w1
    else:
        w1 = (-b + (d ** 0.5)) / 2
        w2 = (-b - (d ** 0.5)) / 2
    answer = [int(max(w1, w2) + 2), int(min(w1, w2) + 2)]
    return answer


print(solution(24, 24)) # [8, 6]
print(solution2(24, 24)) # [8, 6]
