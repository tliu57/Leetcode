class Solution(object):
    def backpackII(self, m, A, V):
	dp = [0 for _ in range(m+1)]
	for i in range(len(A)):
	    for j in range(m, A[i]-1, -1):
		dp[j] = max(dp[j], dp[j-A[i]]+V[i])
	return dp[m]

sol = Solution()
print sol.backpackII(11, [2, 3, 5, 7], [1, 2, 3, 4])

class Solution2(object):
    def backpackII(self, m, A, V):
	n = len(A)
	dp = [[0 for _ in range(m+2)] for _ in range(n+2)]
	for i in range(n+1):
	    for j in range(m+1):
		if i ==0 or j == 0:
			dp[i][j] = 0
		dp[i][j] = dp[i-1][j]
		if j > A[i-1]:
			dp[i][j] = max(dp[i][j], dp[i-1][j-A[i-1]]+V[i-1])
	return dp[n][m]

sol = Solution2()
print sol.backpackII(11, [2, 3, 5, 7], [1, 2, 3, 4])
