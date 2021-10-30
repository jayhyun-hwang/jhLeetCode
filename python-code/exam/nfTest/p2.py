from typing import List

def solution(n: int, jump: int) -> List[int]:
    
    answer = []

    # {"right": 1, "down": 2, "left": 3, "up": 4}
    row = 1
    col = 1

    tlist = [0 for i in range(n*n)]
    num = 1
    tlist[0] = num

    end = len(tlist)-1

    rowEnd = n
    colEnd = n
    jumpNow = 0
    idx = 0
    direct = 1
    while True:
        idx += 1
        if idx >= end:
            for i, val in enumerate(tlist):
                if val == 0:
                    idx = i
        if direct == 1:
            row += 1
            if tlist[idx] == 0:
                jumpNow += 1
                if jumpNow == jump:




        # if direct == 2:

        # if direct == 3:

        # if direct == 4:
    
    # 1 채우기
    return answer
print(solution(5, 3))