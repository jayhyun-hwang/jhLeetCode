# short cut
# print (math.gcd(60,48))

def solution(w:int, h:int) -> int:
    answear = 1

    # greatest common divisor
    gcdArr = [1]

    if w <= h:
        smaller, bigger = w, h
    else:
        smaller, bigger = h, w
    
    # divisor
    div = 2
    while True:
        if smaller % div == 0 and bigger % div == 0:
            smaller /= div
            bigger /= div
            gcdArr.append(div)
        else:
            if div+1 <= smaller:
                div += 1
            else:
                break
    gcd = 1
    for i in gcdArr:
        gcd *= i
    print("gcd",gcd)
    
    # 직사각형에서 지워진 정사각형의 개수, w + h - 최소공배수(1)
    removed = (smaller + bigger -1) * gcd
    print("removed",removed)
    answear = w * h - removed

    return answear

print(solution(8, 12))