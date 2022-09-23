SCORE = 0
BONUS = 1
OPTION = 2


def check_type(str) -> int:
    if str == "S" or str == "D" or str == "T":
        return BONUS
    if str == "#" or str == "*":
        return OPTION
    return SCORE


def solution(str) -> int:
    answer = 0
    score_list = []
    score_idx = 0
    temp_str = ''
    for s in str:
        if check_type(s) == SCORE:
            temp_str += s
            continue
        if check_type(s) == BONUS:
            temp_score = int(temp_str)
            if s == "D":
                temp_score **= 2
            if s == "T":
                temp_score **= 3
            score_list.append(temp_score)
            temp_str = ''
            score_idx += 1
            continue
        if check_type(s) == OPTION:
            if s == "*":
                score_list[score_idx - 1] *= 2
                if score_idx > 1:
                    score_list[score_idx - 2] *= 2
            if s == "#":
                score_list[score_idx - 1] *= -1
    answer = sum(score_list)
    return answer


print(solution('1S2D*3T'))  # 37
print(solution('1D2S#10S'))  # 9
print(solution('1D2S0T'))  # 3
print(solution('1S*2T*3S'))  # 23
print(solution('1D#2S*3S'))  # 5
print(solution('1T2D3D#'))  # -4
print(solution('1D2S3T*'))  # 59
