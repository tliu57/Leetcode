class Solution(object):
	def wallsAndGate(self, rooms):
		for i in range(len(rooms)):
			for j in range(len(rooms)):
				if rooms[i][j] == 0:
					self.bfs(rooms, i, j)
		print rooms

	def bfs(self, rooms, i, j):
		m = len(rooms)
		n = len(rooms[0])
		que = []
		que.append((i, j))
		while not que:
			(ix, jx) = que.pop()
			if isValid((ix-1, jx), rooms):
				rooms[ix-1][jx] = rooms[ix][jx] + 1
				que.append((ix-1, jx))
			if isValid((ix+1, jx), rooms):
				rooms[ix+1][jx] = rooms[ix][jx] + 1
				que.append((ix+1, jx))
			if isValid((ix, jx-1), rooms):
				rooms[ix][jx-1] = rooms[ix][jx] + 1
				que.append((ix, jx-1))
			if isValid((ix, jx + 1), rooms):
				rooms[ix][jx+1] = rooms[ix][jx] + 1
				que.append((ix, jx+1))

	def isValid(self, (ix, jx), rooms):
		m = len(rooms)
		n = len(rooms[0])
		if ix < 0 or jx < 0 or ix > m-1 or jx > n-1 or rooms[ix][jx] == -1 or rooms[ix][jx] == 0:
			return False
		else:
			return True

sol = Solution()
grid = [[3, -1, 0, 1],
     	[2, 2, 1, -1],
	[1, -1, 2, -1],
	[0, -1, 3, 4]]

print sol.wallsAndGate(grid)

