#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

"""
aaaabbcc
NO

aabbcd
NO

aabbccddeefghi
NO

aabbcd
NO

aabbccddeefghi
NO

abcdefghhgfedecba
NO

abc
YES

abcc
YES

abcc
NO
"""




def isValid(s):
    def areTwo(l):
        if  abs(l[0]-l[1])==1 or 1 in l:
            return True
        else:
            return False
            
    freqs = list({ c:s.count(c) for c in set(s) }.values())
    # One char type.. or just one char
    if len(freqs)==1:
         return "YES"
    # Two character types
    elif len(freqs)==2 and areTwo(freqs):
         return "YES"
         
    freqs = { f:freqs.count(f) for f in freqs }
    if len(freqs)==1:
         return "YES"
    if freqs.get(1):
        if freqs[1]>1:
            return "NO"
    elif len(freqs)==2 and areTwo(list(freqs.values())):
         return "YES"
    
    return "NO"


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = isValid(s)

        print(result)


#!/usr/bin/env python

def is_valid_string(s):
    n = list({c:s.count(c)
                for c in s}.values())
    if len(set(n))<2:
        return True
    elif len(set(n))>2:
        return False

    if abs(n[0]-n[1])==1:
        return True
    elif 1 in n:
        return True
    else:
        return False



# Test cases
input_string = input("Enter a string: ")
if is_valid_string(input_string):
    print("Valid string")
else:
    print("Invalid string")
