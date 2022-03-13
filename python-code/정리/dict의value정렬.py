from typing import List


def solution(money: int, costs: List[int]) -> int:
    answer = 0
    unitCost = dict()
    unitCost[1] = costs[0] / 1
    unitCost[5] = costs[1] / 5
    unitCost[10] = costs[2] / 10
    unitCost[50] = costs[3] / 50
    unitCost[100] = costs[4] / 100
    unitCost[500] = costs[5] / 500
    unitCost = sorted(unitCost.items(), key = lambda item: item[1])

    totalCost = 0
    tempMoney = money
    for val in unitCost:
        [quo, rem]=divmod(tempMoney, val[0])
        if quo < 0:
            continue
        totalCost += quo * val[0] * val[1]
        tempMoney = rem
    answer = totalCost
    return answer


print(solution(4578, [1, 4, 99, 35, 50, 1000])) # 2308
