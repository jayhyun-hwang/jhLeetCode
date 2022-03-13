#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'programmerStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


# 파이썬에서 inner 함수를 쓸 때는, 파라미터가 아닌 전역변수의 read만 가능하다. 
# 만약 값을 바꾸는 등 조작하려면 innerfunc에서 nonlocal로 해당 변수를 선언하던가, 파라미터로 넣어줘야 한다.
# 파라미터로 넣어주는게 좋다.(명시적)

def programmerStrings(s):
    # Write your code here
    result = 0
    # 맵으로 하면, key값에 중복값이 들어갈 수 없어, count를 value로 놓고 연산하지 않는 한, 할 일이 많아짐.
    validProgrammer = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r']
    checkProgrammer = set({'p', 'r', 'o', 'g', 'a', 'm', 'e'})
    # checkProgrammer = set(validProgrammer)
    tempArr = validProgrammer.copy()
    # print(checkProgrammer)
    # print(tempArr)
    def checkStrings(s):
        for idx, val in enumerate(s):
            # 셋에서 한번 필터링하여(set의 search: O(1)), 리스트 검사(list search의 복잡도 n)비용을 회피
            if val in checkProgrammer:
                if val in tempArr:
                    tempArr.remove(val)
                    if len(tempArr) == 0:
                        s = s[idx + 1:]
                        return s
    s = checkStrings(s)
    print(s)
    s = s[::-1]
    tempArr = validProgrammer.copy()
    s = checkStrings(s)
    print(s)
    result = len(s)
    return result


print(programmerStrings('prppogxrammerrxproxgrammer'))