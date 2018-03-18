class Solution(object):
	def maxSubArray(self, nums):
		dp = [0 for i in range(len(nums))]
		dp[0] = nums[0] + nums[1]
		maxSum = dp[0]
		for i in range(2, len(nums)):
			incr = nums[i] - nums[i-2]
			dp[i] = incr + dp[i-1] if incr > 0 else dp[i-1]
			maxSum = max(maxSum, dp[i])
		return maxSum

sol = Solution()
print(sol.maxSubArray([-2,-1,-3,4,-1,-5,-2]))
