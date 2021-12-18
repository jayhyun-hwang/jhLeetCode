from typing import List

# 신고 리스트 보고 결과(횟수와 여부) 구현 - 중복 검사
def solution(id_list: List[str], report: List[str], k: int):
    answer = []

    dic1 = dict()
    for rep in report:
        spl = rep.split(" ")
        reporter, reported = spl[0], spl[1]
        if reported not in dic1:
            dic1[reported] = [0,set()]
        if reporter not in dic1[reported][1]:
            dic1[reported][1].add(reporter)
            dic1[reported][0] += 1
    
    print(dic1)

    dic2 = dict()
    for val in dic1.values():
        if val[0] >= k:
            for re in val[1]:
                if re not in dic2:
                    dic2[re] = 0
                dic2[re] += 1
    print(dic2)

    for id in id_list:
        if id in dic2:
            answer.append(dic2[id])
        else:
            answer.append(0)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
 ["muzi frodo", "apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))