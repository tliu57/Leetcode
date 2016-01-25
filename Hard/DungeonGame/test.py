class Solution(object):
	def __init__(self):
		self.res = 0
		self.initial_val = 0
		self.prev_val = 0

	def calculateMinimumHP(self, dungeon):
		if len(dungeon) == 0:
			return 0
		m = len(dungeon)
		n = len(dungeon[0])
		self.dfs(dungeon, 0, 0, m, n, self.initial_val, self.prev_val)
		return self.res
	
	def dfs(self, dungeon, i, j, m, n, initial_val, prev_val):
		if dungeon[i][j] + prev_val <= 0:
			self.initial_val = initial_val - dungeon[i][j] - prev_val + 1
			self.prev_val = 1
		else:
			self.prev_val += dungeon[i][j]
		if i < m - 1:
			self.dfs(dungeon, i+1, j, m, n, self.initial_val, self.prev_val)
		if j < n - 1:
			self.dfs(dungeon, i, j+1, m, n, self.initial_val, self.prev_val)
		if i == m-1 and j == n-1:
			if self.res == 0:
				self.res == self.initial_val
				print "self.res is:", self.res
			else:
				self.res = min(self.res, self.initial_val)
				print "refresh self.res value to:", self.res
			return

sol = Solution()
dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print sol.calculateMinimumHP(dungeon)
