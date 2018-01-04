class Solution(object):
    def backpackIII(self, A, V, m):
	n = len(A)
	dp = [[0 for _ in range(m+2)] for _ in range(n+2)]
	for i in range(1, n+1):
	    for j in range(m+1):
		dp[i][j] = dp[i-1][j]
		if j >= A[i]:
			dp[i][j] = max(dp[i][j-A[i-1]]+V[i-1], dp[i][j])
	return dp[n][m]
