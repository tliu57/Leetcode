class Solution(object):
    def backpackII(self, m, A, V):
	dp = [0 for _ in range(m+1)]
	for i in range(len(A)):
	    for j in range(m, A[i]-1, -1):
		dp[j] = max(dp[j], dp[j-A[i]]+V[i])
	return dp[m]

sol = Solution()
print sol.backpackII(11, [2, 3, 5, 7], [1, 2, 3, 4])
