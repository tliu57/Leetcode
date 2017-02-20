class Solution(object):
	def canPartition(self, nums):
		n = len(nums)
		sum = 0
		for num in nums:
			sum += num
		print "sum is: %d" % sum
		if sum % 2 != 0:
			return False
		sum /= 2
		dp = [False for i in range(sum+1)]
		dp[0] = True
		for num in nums:
			for i in range(sum, 0, -1):
				 if i >= num:
					dp[i] = dp[i] or dp[i-num]
		return dp[sum]

sol = Solution()
nums1 = [1, 5, 11, 5]
print sol.canPartition(nums1)

nums2 = [1, 2, 3, 5]
print sol.canPartition(nums2)
