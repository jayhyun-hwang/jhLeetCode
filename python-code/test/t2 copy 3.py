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
        n = int(convstr)

    print(n)
    # targetList = convstr.split("0")
    while True:
        if n % 10 == 0:

        else:
            
    # for target in targetList:
    #     if len(target) < 1 or target == '1':
    #         continue
    #     target = int(target)
    #     isPrime = True
    #     for i in range(2, target):
    #         if target % i == 0:
    #             isPrime = False
    #             break
    #     if isPrime != True:
    #         continue
    #     answer += 1
    return answer

print(solution(11, 2))
print(solution(437674, 3))
print(solution(110011, 10))