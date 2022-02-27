#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    pStr = ''
    for _ in range(k):
        pStr += n
    #print(pStr)
    p = int(pStr)
    def digitSum(num):
        tempSum = 0
        while True:
            if num < 10:
                return tempSum + num
            else:
                tempSum += num % 10
                num //= 10
    while True:
        if p < 10:
            return p
        else:
            p = digitSum(p)
                    
print(superDigit('9875', 4))
