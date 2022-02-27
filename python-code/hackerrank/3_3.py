#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    answear = []
    alphaList = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    matchAlphaDict = dict()
    for idx, ele in enumerate(alphaList):
        matchAlphaDict[ele] = alphaList[idx - (len(alphaList) - k)]
        matchAlphaDict[ele.upper()] = alphaList[idx -
                                                (len(alphaList) - k)].upper()
    #print(matchAlphaDict)
    for val in s:
        if val in matchAlphaDict:
            answear.append(matchAlphaDict[val])
        else:
            answear.append(val)
    res = ''.join(answear)
    return res

# startTime = time.time() #측정 시작
# result = caesarCipher("middle-Outz", 2)
# print(result)
# endTime = time.time()
# print("time:", endTime - startTime) #수행시간 출력
startTime = time.time() #측정 시작
result = caesarCipher("middle-Outasiovnanvaklnvpovnlasknvlasknvlaskvnlasmz", 5)
print(result)
endTime = time.time()
print("time:", endTime - startTime) #수행시간 출력
