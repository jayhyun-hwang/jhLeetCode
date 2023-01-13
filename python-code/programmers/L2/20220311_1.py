def solution(s):
    answer = ''
    
    sList = s.split(" ")
    numList = []
    for ele in sList:
        numList.append(int(ele))
    answer += str(min(numList))
    answer += " "
    answer += str(max(numList))
    return answer