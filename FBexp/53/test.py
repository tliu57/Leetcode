class Solution(object):
	def maxSubArray(self, nums):
		dp = [0 for i in range(len(nums))]
		dp[0] = nums[0]
		maxSum = nums[0]
		for i in range(1, len(nums)):
			dp[i] = nums[i] + dp[i-1] if dp[i-1] > 0 else nums[i]
			maxSum = max(maxSum, dp[i])
		print dp
		return maxSum

sol = Solution()
print sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print sol.maxSubArray([-2, 1])			
