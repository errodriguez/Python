#!/usr/bin/env python

def find(k, X, Y):
    # To maximize each pair, sort the lists in opposite orders
    A.sort()
    B.sort(reverse=True)
    for a,b in zip(A,B):
        print(a,b, a+b)
        if a+b < k:
            return 'NO'
    return 'YES'

if __name__ == '__main__':

    k = int(input("k: ").strip())
    A = [ int(a) for a in input("A: ").split() ]
    B = [ int(b) for b in input("B: ").split() ]

    print(find(k, A, B))
    
