class Solution(object):
	def isMatch(self, s, p):
		m = len(s)
		n = len(p)
		dp = [[False for i in range(n+1)] for j in range(m+1)]
		dp[0][0] = True
		for i in range(1, m+1):
			dp[i][0] = False
		for j in range(n+1):
			if j > 1:
				dp[0][j] = (p[j-1] == "*") and dp[0][j-2]

		for i in range(1, m+1):
			for j in range(1, n+1):
				if p[j-1] == "*":
					dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == ".") or (s[i-1] == p[j-2]))
				else:
					dp[i][j] = dp[i-1][j-1] or (dp[j-1] == "." or s[i-1] == p[j-1])
		return dp[m][n]

sol = Solution()
print sol.isMatch("a", ".*")

