
import sys

WALL = 2
HOUSE = 1
EMPTY = 0
max_distance = sys.maxint

class Solution():
	def bfs(self, i, j, grid, distances):
		m = len(grid)
		n = len(grid[0])
		dx = [1, 0, -1, 0]
		dy = [0, 1, 0, -1]
		queue = []
		queue.append((i, j))
		visited = set()
		steps = 0
		while queue:
			q_size = len(queue)
			for l in range(q_size):
				curr_x, curr_y = queue.pop(l)
				visited.add((curr_x, curr_y))
				if distances[curr_x][curr_y] != max_distance:
					distances[curr_x][curr_y] += steps
				for w in range(len(dx)):
					next_x = curr_x + dx[w]
					next_y = curr_y + dy[w]
					if self.isValid(next_x, next_y, grid) and (next_x, next_y) not in visited:
						queue.append((next_x, next_y))
			steps += 1
		print distances

	def isValid(self, x, y, grid):
		if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
			return False
		if grid[x][y] != EMPTY:
			return False
		return True

	def shortestDistance(self, grid):
		if not grid:
			return -1
		m = len(grid)
		if m < 1:
			return -1
		n = len(grid[0])
		houses_number = 0
		shortest = sys.maxint
		distances = [[0 for i in range(m)] for j in range(n)]
		for i in range(m):
			for j in range(n):
				if not self.isValid(i, j, grid):
					distances[i][j] = max_distance
				else:
					distances[i][j] = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == HOUSE:
					self.bfs(i, j, grid, distances)
		for i in range(m):
			for j in range(n):			
				if distance[i][j] != max_distance:
					shortest = min(shortest, distances[i][j])
		return shortest


sol = Solution()
sample = [
	  [2, 1, 0],
	  [0, 0, 2],
	  [0, 1, 2]
	]
print sol.shortestDistance(sample)
