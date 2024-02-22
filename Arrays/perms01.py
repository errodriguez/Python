#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    def create(x,l):
        return [ l[0:i] + [x] + l[i:] for i in range(len(l)+1)]
    
    def permutations(a):
        return [[]] if len(a)==0 else [x for y in permutations(a[1:]) for x in create(a[0],y)]
    
    pA = permutations(A)
    pB = permutations(B)

    print(len(pA))
    c = 0
    
    for a in pA:
        c += 1
        for b in pB:
            print(c)
            if False not in [ True if a[i]+b[i]>=k else False for i in range(len(a)) ]:
                return "YES"
    return "NO" 

if __name__ == '__main__':

    sys.setrecursionlimit(2000)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        print(result + '\n')

