class NumMatrix(object):
    def __init__(self, matrix):
	if not matrix:
		return
	m = len(matrix)
	n = len(matrix[0])
	self.sum = [[0 for _ in range(m)]for _ in range(n)]
	for i in range(m):
		self.sum[i][0] = matrix[i][0]
		for j in range(1, n):
	    		self.sum[i][j] = self.sum[i][j-1] + matrix[i][j]
	print self.sum

    def update(self, row, col, val):
	diff = val - matrix[row][col]
	for j in range(col, n):
	    self.sum[row][j] += diff

    def sumRegion(self, row1, col1, row2, col2):
	res = 0
	for i in range(row1, row2+1):
	    res += self.sum[i][col2] - self.sum[i][col1 - 1]
	return res

matrix = [
          [3, 0, 1, 4, 2],
	  [5, 6, 3, 2, 1],
	  [1, 2, 0, 1, 5],
	  [4, 1, 0, 1, 7],
	  [1, 0, 3, 0, 5]
]
sol = NumMatrix(matrix)
print sol.sumRegion(2, 1, 4, 3)
print sol.update(3, 2, 2)
print sol.sumRegion(2, 1, 4, 3)
