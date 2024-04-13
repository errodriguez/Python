#!/usr/bin/env python

"""
How many operations of increase or decrease by 1 are needed to transform an array of N integers into a permutation of the first 1 to N integers?
"""

def operations_to_permutation(arr):
    ops = 0
    sarr = sorted(arr)
    for i in range(len(arr)):
        if i+1 != sarr[i]:
            if sarr[i]<i+1:
                ops += (i+1)-sarr[i]
            else:
                ops += sarr[i]-(i+1)
    return ops

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(operations_to_permutation(arr))

