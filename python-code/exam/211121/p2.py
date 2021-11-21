from typing import List

def solution(names: List[str], homes: List[List[int]], grades: List[float]) -> List[int]:
    answer = []

    dictAll = dict()
    dictGrede = {4:{}, 3:{}, 2:{}, 1:{}}

    for idx in range(len(names)):
        
        #거리 점수 구하기
        #print(homes[idx][0]**2)
        #print(homes[idx][1]**2)
        
        name = names[idx]
        displacement = homes[idx][0]**2 + homes[idx][1]**2
        score = int(grades[idx])


        dictAll[name] = [idx, displacement, score, 0]
        dictGrede[score][name] = displacement
        # 이름으로 바꿈

    rank = 0
    for i in range(4, 0, -1):
        print(dictGrede[i])
        dictGrede[i] = {k: v for k, v in sorted(dictGrede[i].items(), key=lambda item: item[1])}
        print(dictGrede[i])
        temp = sorted(dictGrede[i].keys(), reverse=True)
        print(temp)
        for val in temp:
            rank += 1
            dictAll[dictGrede[i][val]][3] = rank
    print(dictAll)
    
    for val in dictAll:
        answer.append(dictAll[val][3])
    return answer

print("@@@",solution(["azad","andy","louis","will","edward"], [[3,4],[-1,5],[-4,4],[3,4],[-5,0]], [4.19, 3.77, 4.41, 3.65, 3.58]))

# ["azad","andy","louis","will","edward"]	[[3,4],[-1,5],[-4,4],[3,4],[-5,0]]	[4.19, 3.77, 4.41, 3.65, 3.58]	[2,3,1,5,4]
# ["clanguage","csharp","java","python"]	[[3,-3],[-2,7],[-1,-1],[5,4]]	[1.27, 4.31, 4.26, 3.99]	[4,1,2,3]
# ["zzzzzzzzzz"]	[[9999,-9999]]	[1.0]	[1]

# sorted(range(len(names)), key=lambda k: (grades[k], -math.sqrt(homes[k][0]**2 + homes[k][1]**2), names[k]))
