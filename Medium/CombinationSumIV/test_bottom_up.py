class Solution(object):
	def combinationSum4(self, nums, target):
		dp = [0 for i in range(target+1)]
		dp[0] = 1
		for i in range(len(dp)):
			for num in nums:
				dp[i] += dp[i - num] if i - num >= 0 else 0
		return dp[target]

sol = Solution()
print sol.combinationSum4([1,2,3], 4)
			
