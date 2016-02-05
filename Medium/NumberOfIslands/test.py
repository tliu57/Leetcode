class Solution():
	def numIslands(self, grid):
		if not grid:
			return 0
		counter = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					self.dfs(grid, i, j)
					counter += 1

		return counter

	def dfs(self, grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
			return
		if grid[i][j] != 1:
		 	return
		grid[i][j] = 'M'
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)

sol = Solution()
grid = []
grid.append([1,1,0,0,0])
grid.append([1,1,0,0,0])
grid.append([0,0,1,0,0])
grid.append([0,0,0,1,1])
print sol.numIslands(grid)

grid = [1]
print sol.numIslands(grid)

