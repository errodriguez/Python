#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s)%2 != 0:
        return -1
    m = len(s)//2
    c = 0
    l = list(s[m:])
    for i in range(m):
        if s[i] in l:
            l.remove(s[i])
            continue
        c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

