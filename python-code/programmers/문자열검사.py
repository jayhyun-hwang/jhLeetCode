from typing import List

# 전화번호부 prefix 검사

def solution(phone_book: List[str]) -> bool:
    answer = True

    dict1 = {}
    shortestLen = 20
    for val in phone_book:
        if len(val) < shortestLen:
            shortestLen = len(val)
        dict1[val] = True
    #print(dict1)
    #print(shortestLen)
    #print("12313123123"[:3])

    for val in phone_book:
        if len(val) == shortestLen:
            continue
        for i in range(shortestLen, len(val)):
            if val[:i] in dict1:
                return False
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))