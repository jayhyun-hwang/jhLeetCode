from typing import List

def solution(registered_list: List[str], new_id: str) -> str:
    answer = new_id
    strS = ""
    intN = 0
    while True:
        if answer not in registered_list:
            return answer
        else:
            if intN == 0:
                strS = answer
                for idx in range(len(answer)):
                    if answer[idx].isalpha() == False:
                        strS = answer[:idx]
                        if idx < len(answer):
                            intN = int(answer[idx:])
                        break
            intN += 1
            answer = strS + str(intN)

# print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
# print(solution(["apple", "orange", "banana3"],"apple"))

# 설계를 완전하게 끝낸 후 코드 작성하기.