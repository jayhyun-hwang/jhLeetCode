from typing import List


def solution(fees: List[int], records: List[str]):
    answer = []

    dic1 = {}
    carList = list()
    # print(dic1)
    for record in records:
        time = record[:5].split(":")
        hhmm = int(time[0]) * 60 + int(time[1])

        carNum = record[6:10]
        # print(carNum)
        if carNum not in dic1:
            carList.append(carNum)
            dic1[carNum] = [hhmm]
        else:
            dic1[carNum].append(hhmm)
       
    carList.sort()
    for car in carList:
        tlist = dic1[car]
        if len(tlist) % 2 == 1:
            tlist.append(1439)
        i = 0
        feeRes = 0
        time = 0
        while True:
            if i >= len(tlist):
                break
            time += tlist[i+1] - tlist[i]
            i += 2
        feeRes += fees[1]
        if time > fees[0]:
            time -= fees[0]
            q, r = divmod(time, fees[2])
            if r > 0:
                feeRes += (q + 1) * fees[3]
            else:
                feeRes += q * fees[3]
        answer.append(feeRes)
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))