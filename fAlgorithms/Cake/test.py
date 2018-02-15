class Solution(object):
	def canGetCakes(self, num):
		if num < 6 and num >= 0:
			return False
		if num == 6:
			return True
		if num < 9 and num > 6:
			return False
		if num == 9:
			return True
		dp = [False for i in range(num+1)]
		dp[6] = True
		dp[9] = True
		for i in range(10, num+1):
			dp[i] = dp[i-6] or dp[i-9]
		return dp[num]

sol = Solution()
print sol.canGetCakes(26)

