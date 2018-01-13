class NumMatrix(object):
    def __init__(self, matrix):
	if len(matrix) == 0 or len(matrix[0]) == 0:
		return
	n = len(matrix)
	m = len(matrix[0])

	self.dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
	for r in range(n):
	    for c in range(m):
		self.dp[r+1][c+1] = self.dp[r+1][c] + self.dp[r][c+1] + matrix[r][c] - self.dp[r][c]

    def sumRegion(self, row1, col1, row2, col2):
	return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]


matrix = [
[3, 0, 1, 4, 2],
[5, 6, 3, 2, 1],
[1, 2, 0, 1, 5],
[4, 1, 0, 1, 7],
[1, 0, 3, 0, 5]
]
sol = NumMatrix(matrix)
print sol.dp
print sol.sumRegion(2, 1, 4, 3)
