#!/usr/bin/env python

#
# Find the minimum integer greater than cero missed in a list
#
# The function is expected to return an integer.
# The function accepts a list as parameter.
#

def missed0(arr):
    a = sorted(set(arr))
    n = 0
    for i in a:
        n += 1
        if i != n:
           return n
    return n + 1

def missed1(arr):
    a = sorted(set(arr))
    n = 1
    for i in a:
        if i == n:
           n += 1
    return n 

def missed2(arr):
    a = sorted(set(arr))
    if a[0]<1 :
       return 1
    b = set(i for i in range(1,len(a)+1))
    a = b.difference(a) 
    if len(a) == 0:
       return max(b)+1
    else:
       return min(a)

def missed3(arr):
    a = sorted(set(arr))
    if a[0]<1 :
       return 1
    b = {i for i in range(1,len(a)+1)}.difference(a) 
    if len(b) == 0:
       return max(a)+1
    else:
       return min(b)



if __name__ == '__main__':

    print( missed3( list( map(int, input().rstrip().split()) ) ) )
