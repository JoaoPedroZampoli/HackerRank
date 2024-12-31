#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getOutlierValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getOutlierValue(arr):
    # print(arr)
    # Write your code here
    arr.sort()
    # print(arr)
    outlier = -1
    tam = len(arr)-2
    # print("Cópia do Array")
    for i in range(len(arr)):
        temp = arr.copy()
        temp.pop(i)
        # print(temp)
        if sum(temp[0:(len(temp)-1)]) == temp[-1]:
            # print(sum(temp[0:(len(temp)-1)]))
            if outlier < arr[i]:
                outlier = arr[i]
                # print(outlier)
            # else:
            #     print(outlier)            
        # else:
            # print(sum(temp[0:(len(temp)-1)]))
            # print("Não é esse")
    return outlier
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getOutlierValue(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
