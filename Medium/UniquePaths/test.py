class Solution(object):
	def uniquePaths(self, m, n):
		dp = [[1 for i in range(n)] for i in range(m)]
		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
		print dp
		return dp[m-1][n-1]

sol = Solution()
print sol.uniquePaths(7, 3)
