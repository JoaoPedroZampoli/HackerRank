#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximizeTotalMemoryPoints' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY memory as parameter.
#

def maximizeTotalMemoryPoints(memory):
    # Write your code here
    points = memory
    points.sort(reverse=True)
    maxPoints = points[0]
    for i in range(1, len(points)):
        points[i] += points[i-1]
        maxPoints += points[i]
    return maxPoints

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    memory_count = int(input().strip())

    memory = []

    for _ in range(memory_count):
        memory_item = int(input().strip())
        memory.append(memory_item)

    result = maximizeTotalMemoryPoints(memory)

    fptr.write(str(result) + '\n')

    fptr.close()
