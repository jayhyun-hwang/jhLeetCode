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

print(solution(24, 24))