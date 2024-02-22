#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def isPalindrome(s):
    l = len(s)
    i = 0
    j = l-1
    while i<l:
        if s[i]!=s[j]:
            break
        i+=1
        j-=1
    if i>j: return -1
    a = i+1
    b = j
    while a<j and b>i+1:
        if s[a]!=s[b]:
            return j
        a+=1
        b-=1
    return i
#    if s == s[::-1]:
#        return -1
#    middle = (math.ceil(s) if len(s)%2 != 0 else len(s)//2)-1
#    for i in range(middle):
#        if s[i] == s[-(i+1)]:
#            continue
#        elif s[i+1:middle] == s[middle:len(s)-(i+1):-1]:
#            return i
#        elif s[i:middle] == s[middle:len(s)-(i+2):-1]:
#            return len(s)-(i+1)
#        else:
#            return -1
#
#    return -1
        
    

if __name__ == '__main__':

    string = input().strip()

    print(isPalindrome(string))
