def solution(s):
    answer_list = []
    ele_list = s.split(" ")
    for val in ele_list:
        tmp = ""
        for i, char in enumerate(val):
            if i == 0:
                tmp += char.upper()
                continue
            tmp += char.lower()
        answer_list.append(tmp)

    return " ".join(answer_list)
