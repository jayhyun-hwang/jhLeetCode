
class solutionClass:
    def solution(dartResult: str) -> int:
        map1 = {1: 0}
        idx = 1
        isNum = False
        for val in dartResult:
            if val == 'S':
                isNum = False
                map1[idx] **= 1
                idx += 1
            elif val == 'D':
                isNum = False
                map1[idx] **= 2
                idx += 1
            elif val == 'T':
                isNum = False
                map1[idx] **= 3
                idx += 1
            elif val == '*':
                isNum = False
                map1[idx-1] *= 2
                if idx > 1:
                    map1[idx-2] *= 2
            elif val == '#':
                isNum = False
                map1[idx] *= -1
            else:
                if isNum:
                    map1[idx] = int(str(map1[idx])+val)
                else:
                    map1[idx] = int(val)
                isNum = True
        vals = map1.values()
        print("val= ", vals)
        res = sum(vals)
        return res

print(solutionClass.solution("1S2D*3T"))