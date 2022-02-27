#!/bin/python3

# 스트링을 정렬해서 배열로 리턴하는 문법: sorted(str)
import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid: List[str]) -> str:
    # Write your code here
    for i, val in enumerate(grid):
        grid[i] = sorted(val)
    print(grid)
    for idx, _ in enumerate(grid[0]):
        for i in range(len(grid)):
            if i + 1 >= len(grid):
                break
            if ord(grid[i][idx]) <= ord(grid[i + 1][idx]):
                continue
            else:
                return "NO"
    return "YES"

result = gridChallenge(['dcbab', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
print(result)