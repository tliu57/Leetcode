class Solution(object):
	def __init__(self):
		self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

	def longestIncreasingPath(self, matrix):
		rows = len(matrix)
		if rows == 0:
			return 0
		columns = len(matrix[0])
		cache = [[0 for _ in range(columns)] for _ in range(rows)]
		longestLen = 1
		for i in xrange(rows):
			for j in xrange(columns):
				tmpLen = self.dfs(matrix, i, j, rows, columns, cache)
				longestLen = max(tmpLen, longestLen)
		print cache
		return longestLen

	def dfs(self, matrix, i, j, rows, cols, cache):
		if cache[i][j] != 0:
			return cache[i][j]
		maxValue = 1
		for dir in self.dirs:
			x = i + dir[0]
			y = j + dir[1]
			if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] <= matrix[i][j]:
				continue
			lens = 1 + self.dfs(matrix, x, y, rows, cols, cache)
			maxValue = max(maxValue, lens)
		cache[i][j] = maxValue
		return maxValue

sol = Solution()
matrix = [
	[3, 4, 5],
	[3, 2, 6],
	[2, 2, 1]
]
print sol.longestIncreasingPath(matrix)


ex_matrix = [
	[9, 9, 4],
	[6, 6, 8],
	[2, 1, 1]
]		
print sol.longestIncreasingPath(ex_matrix)
