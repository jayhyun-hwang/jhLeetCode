def solution(msg):
    answer = []
    a_dict = dict()
    for i in range(65, 91):
        a_dict[chr(i)] = i - 64
    if len(msg) == 1:
        return [a_dict[msg]]
    temp = ""
    for ele in msg:
        temp += ele
        if temp not in a_dict:
            answer.append(a_dict[temp[:-1]])
            a_dict[temp] = len(a_dict) + 1
            temp = ele
    if temp != "":
        answer.append(a_dict[temp])
    return answer
