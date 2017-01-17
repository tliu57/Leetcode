class Solution(object):
	def __init__(self):
		self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

	def longestIncreasingPath(self, matrix):
		longestLen = 1
		rows = len(matrix)
		if rows == 0:
			return 0
		columns = len(matrix[0])
		cache = [[0] * columns] * rows
		for i in range(0, rows):
			for j in range(0, columns):
				tmpLen = self.dfs(matrix, i, j, rows, columns, cache)
				longestLen = max(tmpLen, longestLen)
		return longestLen

	def dfs(self, matrix, i, j, rows, cols, cache):
		if cache[i][j] != 0:
			return cache[i][j]
		curMax = 1
		for dir in self.dirs:
			x = i + dir[0]
			y = j + dir[1]
			if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] <= matrix[i][j]:
				continue
			maxLen = 1 + self.dfs(matrix, x, y, rows, cols, cache)
			curMax = max(curMax, maxLen)
		cache[i][j] = curMax
		return curMax

sol = Solution()
# matrix = [
#	[3, 4, 5],
#	[3, 2, 6],
#	[2, 2, 1]
# ]
# print sol.longestIncreasingPath(matrix)


ex_matrix = [
	[9, 9, 4],
	[6, 6, 8],
	[2, 1, 1]
]		
print sol.longestIncreasingPath(ex_matrix)
