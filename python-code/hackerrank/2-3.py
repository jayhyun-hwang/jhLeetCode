#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    res = [0 for val in range(100)]
    for val in arr:
        res[val] += 1

    return res

result = countingSort([1,1,3,2,1])
print(result)

