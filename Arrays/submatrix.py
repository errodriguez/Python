#!/usr/bin/env python

from numpy import array, flip

# 414
matrix = array([
                [112, 42, 83, 119],
                [56, 125, 56, 49],
                [15, 78, 101, 43],
                [62, 98, 114, 108]
               ])

# 488
matrix = array([
                [107, 54, 128, 15],
                [12, 75, 110, 138],
                [100, 96, 34, 85],
                [75, 15, 28, 112]
               ])

print(matrix)

n = matrix.shape[0]//2

for c in range(n,2*n):
    if sum(matrix[0:n,c])<sum(matrix[n:2*n,c]):
        matrix[:,c] = flip(matrix[:,c])

for r in range(n):
    if sum(matrix[r][0:n])<sum(matrix[r][2:2*n]):
        matrix[r] = flip(matrix[r])


print(matrix)
print(sum(sum(matrix[:n,:n])))


# Python3 program to find the maximum value
# of top N/2 x N/2 matrix using row and
# column reverse operations


def maxSum(mat):

	Sum = 0
	for i in range(0, R // 2):
		for j in range(0, C // 2):

			r1, r2 = i, R - i - 1
			c1, c2 = j, C - j - 1

			# We can replace current cell [i, j]
			# with 4 cells without changing/affecting
			# other elements.
			Sum += max(max(mat[r1][c1], mat[r1][c2]),
					max(mat[r2][c1], mat[r2][c2]))

	return Sum


# Driver Code
if __name__ == "__main__":

	R = C = 4
	mat = [[112, 42, 83, 119],
		[56, 125, 56, 49],
		[15, 78, 101, 43],
		[62, 98, 114, 108]]

	print(maxSum(mat))
