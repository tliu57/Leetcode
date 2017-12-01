class Solution(object):
	def minTotalDistance(self, grid):
		m = len(grid)
		if m < 1:
			return 0
		n = len(grid[0])
		x_indexes = []
		y_indexes = []
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					x_indexes.append(i)
					y_indexes.append(j)
		x_indexes.sort()
		y_indexes.sort()
		result = self.findMin(x_indexes) + self.findMin(y_indexes)
		return result

	def findMin(self, indexes):
		start = 0
		end = len(indexes)-1
		res = 0
		while start < end:
			res += indexes[end] - indexes[start]
			end -= 1
			start += 1
		return res

grid = [
	[1, 0, 0, 0, 1],
	[0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0]
]
sol = Solution()
print sol.minTotalDistance(grid)
