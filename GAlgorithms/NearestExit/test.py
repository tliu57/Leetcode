INF = 2147483647

class Solution:

	def wallsAndGates(self, rooms):
		m = len(rooms)
		if m < 1:
			return
		n = len(rooms[0])
		if n < 1:
			return
		queue = []
		for i in range(m):
			for j in range(n):
				if rooms[i][j] == 0:
					queue.append((i, j))

		dx = [1, 0, -1, 0]
		dy = [0, 1, 0, -1]
		while queue:
			cur_x, cur_y = queue.pop(0)
			for i in range(4):
				next_x = cur_x + dx[i]
				next_y = cur_y + dy[i]
				if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n and rooms[next_x][next_y] == INF:
					rooms[next_x][next_y] = rooms[cur_x][cur_y] + 1
					queue.append((next_x, next_y))


sol = Solution()
grid = [
	[INF, -1, 0, INF],
	[INF, INF, INF, -1],
	[INF, -1, INF, -1],
	[0, -1, INF, INF]
	]

sol.wallsAndGates(grid)
print grid
