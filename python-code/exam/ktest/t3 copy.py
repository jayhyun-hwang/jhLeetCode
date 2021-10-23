from typing import List
import collections

def solution(n: int, k: int):
    answer = 0
    
    if k < 10:
        conv = collections.deque()
        while True:
            rem = n % k
            conv.appendleft(str(rem))
            n = n // k
            if n < k:
                conv.appendleft(str(n))
                break
        convstr = ''.join(conv)
    else:
        convstr = str(n)

    targetList = convstr.split("0")

    for target in targetList:
        if len(target) < 1 or target == '1':
            continue
        target = int(target)
        isPrime = True
        for i in range(2, target):
            if target % i == 0:
                isPrime = False
                break
        if isPrime != True:
            continue
        answer += 1
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))