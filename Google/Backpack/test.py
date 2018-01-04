class Solution(object):
    def backpack(self, m, A):
	dp = [[False for _ in range(m+2)] for _ in range(len(A)+2)]
	dp[0][0] = True
	for i in range(1, len(A)+1):
	    for j in range(m+1):
		dp[i][j] = dp[i-1][j]
		if j >= A[i-1] and dp[i-1][j-A[i-1]]:
			dp[i][j] = True
	for i in range(m, -1, -1):
	    if dp[len(A)][i] == True:
	    	return i
	return 0

sol = Solution()
print sol.backpack(11, [2, 3, 5, 7])

class Solution2(object):
    def backpack(self, m, A):
	dp = [0 for _ in range(m+1)]

	for i in range(len(A)):
	    for j in range(m, A[i]-1, -1):
		dp[j] = max(dp[j], dp[j-A[i]] + A[i])
	return dp[m]

sol2 = Solution2()
print sol2.backpack(11, [2, 3, 5, 7])
