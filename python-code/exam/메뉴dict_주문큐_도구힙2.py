import collections
from typing import List


def solution(n: int, recipes: List[str], orders: List[str]) -> int:
    answer = 0

    # 레시피 딕셔너리
    recTimeDict = dict()
    for rec in recipes:
        mandt = rec.split(" ")
        recTimeDict[mandt[0]] = int(mandt[1])
    print(recTimeDict)

    # 주문 큐
    orderQue = collections.deque()
    for val in orders:
        order = val.split(" ")
        orderQue.append([order[0], int(order[1])])
    print(orderQue)

    # 화로 n 리스트
    tools = [0 for i in range(n)]
    print(tools)

    time = 1
    pri = orderQue.popleft()
    while True:
        for idx, val in enumerate(tools):
            if time >= val:
                tools[idx] = 0
        if time >= pri[1]:
            for idx, val in enumerate(tools):
                if val > 0:
                    continue
                else:
                    print("요리시작", time)
                    tools[idx] = time + recTimeDict[pri[0]]
                    if len(orderQue) < 1:
                        return max(tools)
                    pri = orderQue.popleft()
                    break
        print(tools)
        time += 1

    return answer


print(solution(2, ["A 3", "B 2"], ["A 1", "A 2", "B 3", "B 4"]))
print(solution(3, ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"], [
      "PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]))
