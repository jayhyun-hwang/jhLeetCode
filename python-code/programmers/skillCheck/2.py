
from cgi import MiniFieldStorage
import collections
from typing import List


def solution(n: int, wires: List[List[int]]) -> int:
    answer = -1
    tempArr = []
    
    for val in wires:
        tempArr = wires.copy()
        tempArr.remove(val)
        minDif = n
        for val2 in tempArr:
            forDif1 = searchTemp(val[0], tempArr, 1)
            forDif2 = searchTemp(val[1], tempArr, 1)
            dif = abs(forDif1 - forDif2)
            if dif < minDif:
                minDif = dif
    answer = minDif
    return answer

def searchTemp(targetNum: int, tempArr: List[List[int]], nodes: int) -> int:
    for eleList in tempArr:
        if targetNum in eleList:
            nodes += 1
            tempArr.remove(eleList)
            tempRemoved = eleList.copy()
            tempRemoved.remove(targetNum)
            searchTemp(tempRemoved.pop(), tempArr, nodes)


    return nodes
	
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))