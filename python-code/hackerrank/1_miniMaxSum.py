#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr: List[int]):
    # Write your code here
    arrSum = sum(arr)
    minSum = arrSum - max(arr)
    maxSum = arrSum - min(arr)

    print(minSum, maxSum)
miniMaxSum(arr)
