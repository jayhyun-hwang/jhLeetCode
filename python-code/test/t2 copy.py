import collections


def solution(n: int, k: int):
    answer = 0

    conv = ""
    while n > 0:
        rem = int(n%k)
        conv += str(rem)
        n //= k
    conv = conv[::-1]
    targetList = conv.split("0")
    print(targetList)

    for target in targetList:
        if len(target) < 1 or target == '1':
            continue
        target = int(target)
        isPrime = True
        for i in range(2, target):
            if target % i == 0:
                isPrime = False
                break
        if isPrime == True:
            answer += 1
    return answer

def convNum(n, b):
    qual = n // b
    rem = n % b
    if qual == 0:
        return rem
    else:
        return convNum(qual, b) + rem

print(solution(11, 2))
print(solution(437674, 3))
print(solution(110011, 10))
print(solution(6, 9))
print(solution(1, 3))
print(solution(1, 10))
print(solution(1000000, 3))
print(solution(1000000, 10))
