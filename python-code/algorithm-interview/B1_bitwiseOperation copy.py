from typing import List

class solutionClass:
    def solution(n: int, arr1:List[int], arr2:List[int]) -> List[str]:
        answer = []
        for i in range(n):
            nb = bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' ')
            answer.append(nb)
        return answer

print(solutionClass.solution(5, [9,20,28,18,11], [30,1,21,17,28]))
