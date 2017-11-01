class Solution:
	def __init__(self):
		self.ans = []

	def getFactors(self, n):
		self.dfs(2, n, [])
		return self.ans

	def dfs(self, start, remain, path):
		if start == remain:
			if path:
				self.ans.append([elem for elem in path])
		for i in range(start, remain + 1):
			if remain % start == 0:
				path.append(start)
				self.dfs(start, remain/start)
				path.pop()
