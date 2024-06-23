#! /usr/bin/env python

def solve(l):
    A = set(l) 
    if max(A)<0:
        return 1
    B = set(range(min(l), max(l)+2))
    return min(B.difference(A)) 


if __name__ == '__main__':

    assert solve([1, 3, 6, 4, 1, 2]) == 5
    assert solve([1, 2, 3]) == 4
    assert solve([-1, -3]) == 1
    assert solve([17, 20, 21, 23, 27, 30]) == 18
