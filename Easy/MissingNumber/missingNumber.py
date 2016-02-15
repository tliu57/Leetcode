class Solution(object):
	def missingNumber(self, nums):
		n = len(nums)
		sum1 = 0
		sum2 = 0
		for i in range(n):
			sum1 += i
			sum2 += nums[i]
		sum1 += n
		return sum1 - sum2

sol = Solution()
nums = [0, 1, 3]
print sol.missingNumber(nums)
