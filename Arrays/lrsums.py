#!/usr/bin/env python

"""
export OUTPUT_PATH=/dev/stdout
"""

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Expensive approach
#def balancedSums(arr):
#    for i in range(len(arr)):
#        print(i, arr[:i], arr[i+1:]) 
#        if sum(arr[:i]) == sum(arr[i+1:]):
#            return "YES"
#
#    return "NO"

def balancedSums(arr):
    right = sum(arr)
    left = 0
    for i in arr:
        right -= i
        if left == right:
            return "YES"
        else:
            left += i
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

