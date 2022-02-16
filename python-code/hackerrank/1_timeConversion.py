#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s: str):
    # Write your code here
    hour = int(s[:2])
    tm = s[-2:]
    hourStr = ""

    if tm == "PM":
        if hour != 12:
            hour = hour + 12
    else:
        if hour == 12:
            hour = 0
    hourStr = str(hour).zfill(2)
    s = hourStr + s[2:-2]

    print(s)
    # print(t)
    # print(tm)


timeConversion("07:05:45PM")
timeConversion("12:01:00PM")
timeConversion("12:01:00AM")