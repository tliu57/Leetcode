class Solution():
	def solveNQueens(self, n):
		self.board = [-1 for i in range(n)]
		self.res = []
		self.dfs(0, [], n)
		return self.res

	def dfs(self, depth, valuelist, n):
		if depth == n:
			self.res.append(valuelist)
			return
		for i in range(n):
			if self.check(depth, i):
				self.board[depth] = i
				s = '.' * n
				self.dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]], n)

	def check(self, depth, Q_pos):
		for i in range(depth):
			if self.board[i] == Q_pos or abs(depth - i) == abs(self.board[i] - Q_pos):
				return False
		return True

sol = Solution()
print sol.solveNQueens(4)
