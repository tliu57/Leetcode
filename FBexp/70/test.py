class Solution(object):
	def __init__(self):
		self.dp = []

	def climbStairs(self, n):
		self.dp = [-1 for i in range(n+1)]
		self.dp[0] = 0
		if n >= 1:
			self.dp[1] = 1
		if n >= 2:
			self.dp[2] = 2
		res = self.helper([1, 2], n)
		return res
	
	def helper(self, candidates, target):
		if self.dp and self.dp[target] != -1:
			return self.dp[target]
		res = 0
		for i in candidates:
			if target - i >= 0:
				res += self.helper(candidates, target - i)
		self.dp[target] = res
		return self.dp[target]

sol = Solution()
print sol.climbStairs(3)
