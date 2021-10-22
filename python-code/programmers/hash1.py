import collections
from typing import List

def solution(participant: List[str], completion: List[str]) -> str:
    answear = ""
    checkDict = collections.defaultdict(int)
    for cval in completion:
        checkDict[cval] += 1

    for pval in participant:
        if checkDict[pval] < 1:
            answear =  pval
            break
        checkDict[pval] -= 1
    
    return answear

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))