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

def timeConversion(s):
    # Write your code here
    military_hour = ""
    time_convert = {
        "01": "13",
        "02": "14",
        "03": "15",
        "04": "16",
        "05": "17",
        "06": "18",
        "07": "19",
        "08": "20",
        "09": "21",
        "10": "22",
        "11": "23",
        "12": "12",
    }
    s_split = s.split(":")
    if s_split[2][-2:] == "PM":
        military_hour = time_convert[s_split[0]]
        military_hour+=(":" + str(s_split[1]) + ":" + s_split[2][:2])
    
    elif s_split[2][-2:] == "AM" and s_split[0] == "12":
        military_hour+=("00" + ":" + str(s_split[1]) + ":" + s_split[2][:2])

    else:
       military_hour+=s[:-2]     
        
    return military_hour
    

def anotherTimeConversion(s):
    h = int(s[:2])
    msec = s[2:8]
    h = h % 12 if s[-2:] == 'AM' else h % 12 + 12
    return f"{h:02}{msec}"

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()