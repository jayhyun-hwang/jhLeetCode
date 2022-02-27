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
    a1 = sum(int(x) for x in n)
    print("a1", a1)
    print("a1 * k", a1 * k)
    val = (k * a1 - 1) % 9
    print("val", val)
    return 1 + val


print(superDigit('9875', 4))
