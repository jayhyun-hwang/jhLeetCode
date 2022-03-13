import collections
from typing import List

# 중복 count 제한으로 숫자 세기

def solution(id_list: List[str], k: int) -> int:
    
    answer = 0

    dict1 = collections.defaultdict(int)
    # 문자열 split, set에 넣기
    for day_id_list in id_list:
        tempset = set(day_id_list.split(" "))
        for val in tempset:
            if dict1[val] < k:
                dict1[val] += 1
    
    answer = sum(dict1.values())
    return answer

print(solution(["A B C D", "A D", "A B D", "B D"], 2))
print(solution(["A"], 2))
print(solution(["A B C D", "A D", "A B D", "B D"], 2))
