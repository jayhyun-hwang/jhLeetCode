from typing import List

def solution(skill: str, skill_trees: List[str]) -> int:
    answer = -1
    skillOrder = list(skill)
    skillOderedDict = dict()
    for val in skill:
        skillOderedDict[val] = True

    print(skillOrder)
    print(skillOderedDict)
    

    resCount = 0
    for ele in skill_trees:
        skillIdx = 0
        isValid = True
        for chr in ele:
            if chr in skillOderedDict:
                if chr == skillOrder[skillIdx]:
                    skillIdx += 1
                else:
                    isValid = False
                    break
        if isValid:
            resCount += 1

    answer = resCount
    print(answer)
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])