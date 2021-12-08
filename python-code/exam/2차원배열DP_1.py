from typing import List

def solution(drum: List[str]) -> int:
    answer = 0
    array = [["" for col in range(len(drum))] for row in range(len(drum))]
    
    for r, row in enumerate(drum):
        for idx, val in enumerate(row):
            array[r][idx] = val
    # print(array)

    for idx in range(len(array[0])):
        row = 0
        col = idx
        starLimit = 0
        # print(idx)
        while True:
            # 만족하면 리턴
            if row >= len(array):
                answer += 1
                break
            val = array[row][col]
            if val == '#':
                row += 1
            elif val == '*':
                if starLimit == 1:
                    break
                starLimit += 1
                row += 1
            elif val == '<':
                col -= 1
            elif val == '>':
                col += 1
    return answer



print(solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"]))