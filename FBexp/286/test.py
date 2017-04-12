INF = 2147483647

class Solution(object):
	def wallsAndGates(self, rooms):
		if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
			return
		m = len(rooms)
		n = len(rooms[0])
		self.queue = []
		for i in range(m):
			for j in range(n):
				if rooms[i][j] == 0:
					self.queue.append((i, j))

		while self.queue:
			i, j = self.queue.pop(0)
			if i > 0 and rooms[i-1][j] == INF:
				rooms[i-1][j] = rooms[i][j] + 1
				self.queue.append((i-1, j))
			if j > 0 and rooms[i][j-1] == INF:
				rooms[i][j-1] = rooms[i][j] + 1
				self.queue.append((i, j-1))
			if i < m - 1 and rooms[i+1][j] == INF:
				rooms[i+1][j] = rooms[i][j] + 1
				self.queue.append((i+1, j))
			if j < n - 1 and rooms[i][j+1] == INF:
				rooms[i][j+1] = rooms[i][j] + 1
				self.queue.append((i, j+1))

sol = Solution()
rooms = [
	 [INF, -1, 0, INF],
	 [INF, INF, INF, -1],
	 [INF, -1, INF, -1],
	 [0, -1, INF, INF]	
	]
sol.wallsAndGates(rooms)
print rooms
