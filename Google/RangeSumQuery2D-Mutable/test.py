class NumMatrix(object):
    def __init__(self, matrix):
	if not matrix:
		return
	self.m, self.n = len(matrix), len(matrix[0])
	self.matrix = [[0] * (self.n) for _ in range(self.m)]
	self.bit = [[0] * (self.n+1) for _ in range(self.m+1)]
	for i in range(self.m):
	    for j in range(self.n):
		self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
	diff = val - self.matrix[row][col]
	self.matrix[row][col] = val
	i = row + 1
	while i <= self.m:
		j = col + 1
		while j <= self.n:
			self.bit[i][j] += diff
			j += (j & -j)
		i += (i & -i)

    def sumRegion(self, row1, col1, row2, col2):
	return self.sumCorner(row2, col2) + self.sumCorner(row1-1, col1-1) - self.sumCorner(row1-1, col2) - self.sumCorner(row2, col1-1)

    def sumCorner(self, row, col):
	res = 0
	i = row+1
	while i:
		j = col + 1
		while j:
			res += self.bit[i][j]
			j -= (j&-j)
		i -= (i&-i)
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

