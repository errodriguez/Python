#!/usr/bin/env python

def cuts(bar, day, month):
    ways=0
    for i in range(0,len(bar)):
        print(bar[i:i+month])
        if sum(bar[i:i+month])==day:
            ways+=1
    return ways


if __name__ == '__main__':

    bar = [ int(a) for a in input("squares: ").split() ]
    day = int(input("day: ").strip())
    month = int(input("month: ").strip())

    print(cuts(bar, day, month))
    
