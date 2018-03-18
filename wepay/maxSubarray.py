class Solution(object):
	def maxSubArray(self, nums):
		dp = [0 for i in range(len(nums))]
		dp[1] = nums[0] + nums[1]
		maxSum = dp[0]
		for i in range(2, len(nums)):
			dp[i] = nums[i] + nums[i-1]
			if dp[i-1] - nums[i-1] > 0: 
				dp[i] += dp[i-1] - nums[i-1]
			maxSum = max(maxSum, dp[i])
		return maxSum

sol = Solution()
print(sol.maxSubArray([-2,-1,-3,4,-1,-5,-2]))
