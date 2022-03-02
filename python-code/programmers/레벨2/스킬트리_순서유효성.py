from typing import List

# 주어진 스킬 순서로 스킬트리 유효성 검사
def solution(skill: str, skill_trees: List[str]) -> int:
    answer = -1
    # 순서 str를 리스트화
    skillOrder = list(skill)
    # set이 더 간결해 보임
    skillOderedDict = set(skill)
    # 순서가 있는 스킬들을 dict에 삽입
    # for val in skill:
    #     # skillOderedDict[val] = True
    #     skillOderedDict.add(val)

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