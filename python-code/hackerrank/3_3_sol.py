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
    result = ""
    for i in range(len(s)):
        char = s[i]

        # Encrypt uppercase characters
        if char.isalpha() == False:
            result += s[i]
            continue
        if (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)

    return result


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