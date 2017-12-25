import sys

class Solution(object):
    def shortestDistance(self, grid):
	m = len(grid)
	if m < 1:
		return 0
	n = len(grid[0])
	dist = [[sys.maxint for j in range(n)] for i in range(m)]
	reachable_count = [[0 for j in range(n)] for i in range(m)]
	min_dist = sys.maxint

	buildings = 0
	for i in range(m):
	    for j in range(n):
		if grid[i][j] == 1:
			self.bfs(grid, i, j, m, n, dist, reachable_count)
			buildings += 1
	for i in range(m):
	    for j in range(n):
		if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
			min_dist = dist[i][j]
	return min_dist if min_dist != sys.maxint else -1

    def bfs(self, grid, i, j, m, n, dist, reachable_count):
	visited = [[False for y in range(n)]for x in range(m)]
	visited[i][j] == True
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	queue = []
	queue.append((i, j, 0))
	while queue:
		curr_x, curr_y, curr_d = queue.pop(0)
		if dist[curr_x][curr_y] == sys.maxint:
			dist[curr_x][curr_y] = 0
    		dist[curr_x][curr_y] += curr_d
		for l in range(len(dx)):
		    next_x = curr_x + dx[l]
		    next_y = curr_y + dy[l]
		    if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n and not visited[next_x][next_y]:
		    	visited[next_x][next_y] = True
		    	if grid[next_x][next_y] == 0:
		    		queue.append((next_x, next_y, curr_d + 1))
		    		reachable_count[next_x][next_y] += 1
		

sol = Solution()
grid = [
	[1, 0, 2, 0, 1],
	[0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0]
]
print sol.shortestDistance(grid)
