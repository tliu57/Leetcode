class Solution(object):
    def maximalSquare(self, matrix):
	m = len(matrix)
	n = len(matrix[0])
	maxsize = 0
	size = [[0 for _ in range(n+1)] for _ in range(m+1)]
	for j in range(n):
	    size[0][j] = matrix[0][j] - '0'
	    maxsize = max(maxsize, size[0][j])
	for i in range(m):
	    size[i][0] = matrix[i][0] - '0'
	    maxsize = max(maxsize, size[i][0])
	for i in range(1, m):
	    for j in range(1, n):
		if matrix[i][j] == '1':
			size[i][j] = min(size[i-1][j-1], size[i][j-1], size[i-1][j]) + 1
			maxsize = max(maxsize, size[i][j])
	return maxsize * maxsize

