class Solution(object):
	def countBits(self, num):
		if num == 0:
			return [0]
		dp = [0 for i in range(num+1)]
		dp[0] = 0
		dp[1] = 1
		for i in range(2, num+1):
			dp[i] = dp[i%2] + dp[i/2]
		res = []
		for i in range(num+1):
			res.append(dp[i])
		return res

sol = Solution()
print sol.countBits(5)
