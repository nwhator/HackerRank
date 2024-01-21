#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Size of square matrix
    n = len(arr)
    
    # Initialize sum of Left-to-right and Right-to-left diagonals
    ltr = sum(arr[i][i] for i in range(n))
    rtl = sum(arr[i][n - 1 - i] for i in range(n))
    
    # Return absolute difference
    return abs(ltr - rtl)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
