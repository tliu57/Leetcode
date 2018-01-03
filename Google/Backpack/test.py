class Solution(object):
    def backpack(self, m, A):
	dp = [0 for _ in range(m+1)]
	dp[0] = 1
	ans = 0
	for item in A:
		for i in range(m, -1, -1):
		    if i-item >= 0 and dp[i-item] > 0:
		    	ans = max(ans, i)
		    	dp[i] = 1
	return ans

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
