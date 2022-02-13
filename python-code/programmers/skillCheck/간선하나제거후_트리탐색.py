
from cgi import MiniFieldStorage
import collections
from typing import List


def solution(n: int, wires: List[List[int]]) -> int:
    answer = -1
    removedList = []
    minDif = n
    for removed in wires:
        removedList = wires.copy()
        removedList.remove(removed)
        
        node1 = removed[0]
        visited1 = []
        searchDFS(node1, removedList, visited1)
        num1 = len(visited1)
        node2 = removed[1]
        visited2 = []
        searchDFS(node2, removedList, visited2)
        num2 = len(visited2)
        thisDif = abs(num1 - num2)

        if minDif > thisDif:
            minDif = thisDif

    answer = minDif
    return answer
	
def searchDFS(targetNum: int, removedList: List[List[int]], visited: List[int]):
    if targetNum not in visited:
        visited.append(targetNum)
    for edge in removedList:
        if targetNum in edge:
            tempEdge = edge.copy()
            linkedNum = tempEdge.remove(targetNum)
            if linkedNum not in visited:
                searchDFS(tempEdge.pop(), removedList, visited)
            else:
                return
    return 
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))