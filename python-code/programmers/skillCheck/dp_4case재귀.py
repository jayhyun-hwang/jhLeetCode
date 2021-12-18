from typing import List

def solution(arr: List[List[int]]) -> List[int]:
    answer = [0,0]
    if len(arr) == 1:
        if arr[0][0] == 0:
            return [1,0]
        else:
            return [0,1]
    #정사각 2차 배열    
    n = len(arr)
    tempArr = arr
    def comp(row: int, col: int, leng: int):
        val = arr[row][col]
        for rowIdx in range(row, row+leng):
            for colIdx in range(col, col+leng):
                if arr[rowIdx][colIdx] != val:
                    leng //= 2
                    comp(row, col, leng)
                    comp(row, col + leng, leng)
                    comp(row + leng, col, leng)
                    comp(row + leng, col + leng, leng)
                    return
        answer[val] += 1
    comp(0, 0, n)
    return answer

# print("exception",solution([[0]]))
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) #4, 9
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])) # 10, 15