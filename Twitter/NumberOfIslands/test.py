class Solution(object):
    def numIslands(self, grid):
	m = len(grid)
	if m < 1:
		return 0
	n = len(grid[0])
	count = 0
	for i in range(m):
	    for j in range(n):
		if grid[i][j] == 1:
			count += 1
			self.bfs(grid, i, j)
	return count


    def bfs(self, grid, i, j):
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	queue = []
	queue.append((i, j))
	while queue:
	    curr_x, curr_y = queue.pop(0)
	    grid[curr_x][curr_y] = 0
	    for i in range(len(dx)):
	        new_x = curr_x + dx[i]
		new_y = curr_y + dy[i]
		if self.valid(grid, new_x, new_y) and grid[new_x][new_y] == 1:
		    queue.append((new_x, new_y))

    def valid(self, grid, x, y):
	m = len(grid)
	n = len(grid[0])
	if x < 0 or x >= m:
		return False
	if y < 0 or y >= n:
		return False
	return True

sol = Solution()
grid = [
	[1, 1, 1, 1, 0],
	[1, 1, 0, 1, 0],
	[1, 1, 0, 0, 0],
	[0, 0, 0, 0, 0]
]
print sol.numIslands(grid)
grid2 = [
	 [1, 1, 0, 0, 0],
	 [1, 1, 0, 0, 0],
	 [0, 0, 1, 0, 0],
	 [0, 0, 0, 1, 1]
]
print sol.numIslands(grid2)
