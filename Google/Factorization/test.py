class Solution:
	def __init__(self):
		self.ans = []

	def getFactors(self, n):
		self.dfs(2, n, [])
		return self.ans

	def dfs(self, start, remain, path):
		if remain == 1:
			if path and path not in self.ans and len(path) > 1:
				self.ans.append([elem for elem in path])
		import math
		for i in range(start, int(math.sqrt(remain)) + 1):
			if remain % i == 0:
				path.append(i)
				self.dfs(i, remain/i, path)
				path.pop()
		if remain >= start:
			path.append(remain)
			self.dfs(remain, 1, path)
			path.pop()

sol = Solution()
print sol.getFactors(1073741824)
