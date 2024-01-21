#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    postiveCount = sum(1 for num in arr if num > 0)
    negativeCount = sum(1 for num in arr if num < 0)
    zeroCount = sum(1 for num in arr if num == 0)
    
    # Calculate ratios
    totalElements = len(arr)
    postiveRatio = postiveCount / totalElements
    negativeRatio = negativeCount / totalElements
    zeroRatio = zeroCount / totalElements
    
    print(f'{postiveRatio:.6f}')
    print(f'{negativeRatio:.6f}')
    print(f'{zeroRatio:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
