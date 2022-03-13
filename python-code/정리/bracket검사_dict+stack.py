#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'matchingBraces' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY braces as parameter.
#

def matchingBraces(braces):
    # Write your code here
    res = []
    bStack = []
    openDict = dict({
        '{': '}',
        '[': ']',
        '(': ')',
    })
    for strEle in braces:
        bStack = []
        isValid = True
        for ele in strEle:
            if ele in openDict:
                bStack.append(ele)
            else:
                if len(bStack) < 1:
                    isValid = False
                    break
                poped = bStack.pop()
                if openDict[poped] != ele:
                    isValid = False
                    break
        if isValid and len(bStack) == 0:
            res.append('YES')
        else:
            res.append('NO')
        
    return res
result = matchingBraces(['[]{}()()]', '()', '[]{}()', '[[[]]{}]'])
print(result)
