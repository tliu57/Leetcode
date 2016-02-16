import pdb
INF = 2147483647

class Solution(object):
	def wallsAndGates(self, rooms):
		self.que = []
		for i in range(len(rooms)):
			for j in range(len(rooms[0])):
				if rooms[i][j] == 0:
					self.que.append((i, j))
		dir = [[-1, 0, 1, 0],
			[0, -1, 0, 1]]
		while len(self.que) != 0:
			(i, j) = self.que.pop()
			for delta in range(len(dir[0])):
			    new_i = i + dir[0][delta]
			    new_j = j + dir[1][delta]
			    if new_i < 0 or new_i >= len(rooms) or new_j < 0 or new_j >= len(rooms[0]) or rooms[new_i][new_j] == 0 or rooms[new_i][new_j] == -1:
				continue
			    if rooms[new_i][new_j] < rooms[i][j] + 1:
			    	continue
			    rooms[new_i][new_j] = rooms[i][j] + 1
			    self.que.append((new_i,new_j))
		return rooms

sol = Solution()
grid = [[INF, -1, 0, INF],
     	[INF, INF, INF, -1],
	[INF, -1, INF, -1],
	[0, -1, INF, INF]]
print sol.wallsAndGates(grid)
