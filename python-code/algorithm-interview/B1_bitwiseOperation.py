from typing import List

# 파이썬의 진법 표현
# bin(87) ==> '0b1010111'
# int('0b1010111', 2) ==> 87
# 이진수임을 표현하는 0b는 생략가능

def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    maps=[]
    for i in range(n):
        #OR 연산 후 이진수 변환
        maps.append(
            bin(arr1[i] | arr2[i])[2:]  # binary 함수, bin( & ), bin( | ), bin( + ), bin( * ), bin( >> ), bin( << ), bin ( ^ ) - XOR, 두 값이 다를 때 참
                .zfill(n)   # n자리수로 만드는 함수, 부족한 만큼 앞에 0을 채운다.
                .replace('1', '#')  # replace는 replaceAll, 세번째 arg에 숫자를 넣으면 횟수만큼만 replace를 수행한다.
                .replace('0', ' ')  # ex) text.replace("-", "", 3)
        )
    return maps


print(solution(5, [9,20,28,18,11], [30, 1, 21, 17, 28]))
