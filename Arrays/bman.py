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
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    def printGrid():
        for row in grid:
            for col in row:
                print(col, end="")
            print()

    def scanGrid():
        return { (r,c)
                    for r in range(len(grid))
                        for c in range(len(grid[r]))
                            if grid[r][c]=='O'
               }

    def makeGrid0():
        return { (i,j) for i in range(len(grid)) for j in range(len(grid[i])) }



    printGrid()
    print(makeGrid0())
    print()
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
