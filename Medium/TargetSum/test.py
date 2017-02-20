class Solution(object):
	def findTargetSumWays(self, nums, S):
		# Subset(P) + Subset(N) == sum
		# Subset(P) - Subset(N) == S
		# 2* Subset(P) == sum + S
		# Subset(P) == (sum + S)/2

		sum = 0
		for num in nums:
			sum += num
		if sum < S or (sum + S) % 2 != 0:
			return 0
		# Find how many subsets sums up to (sum + S)/2
		target = (sum + S)/2
		dp = [0 for i in range(target+1)]
		dp[0] = 1
		for num in nums:
			for i in range(target, num - 1, -1):
				dp[i] += dp[i - num]
		return dp[target]

sol = Solution()
nums = [1, 1, 1, 1, 1]
S = 3
print sol.findTargetSumWays(nums, S)

nums2 = [1, 2, 7, 9, 981]
S2 = 1000000000
print sol.findTargetSumWays(nums2, S2)

nums3 = [0, 0, 0, 0, 0, 0, 0, 0, 1]
S3 = 1
print sol.findTargetSumWays(nums3, S3)
