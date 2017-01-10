class Solution(object):
	def numIslands(self, grid):
		m = len(grid)
		if m == 0:
			return 0
		n = len(grid[0])
		count = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					count += 1
					self.bfsCheck(grid, i, j)
		return count

	def bfsCheck(self, grid, i, j):
		queue = []
		queue.append((i,j))
		grid[i][j] = 0
		while len(queue) != 0:
			node = queue.pop(0)
			x = node[0]
			y = node[1]
			if y > 0 and grid[x][y-1] == 1:
				queue.append((x, y-1))
				grid[x][y-1] = 0	
			if y < len(grid[0])-1 and grid[x][y+1] == 1:
				queue.append((x, y+1))
				grid[x][y+1] = 0
			if x > 0 and grid[x-1][y] == 1:
				queue.append((x-1, y))
				grid[x-1][y] = 0
			if x < len(grid)-1 and grid[x+1][y] == 1:
				queue.append((x+1, y))
				grid[x+1][y] = 0
			

sol = Solution()
grid = []
grid.append([1, 1, 1, 1, 0])
grid.append([1, 1, 0, 1, 0])
grid.append([1, 1, 0, 0, 0])
grid.append([0, 0, 0, 0, 0])

print sol.numIslands(grid)

	
