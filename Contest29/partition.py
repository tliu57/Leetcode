class Solution(object):
	def arrayPairSum(self, nums):
		sum = 0
		nums.sort()
		for i in range(len(nums)):
			if i % 2 == 0:
				sum += nums[i]
		return sum

sol = Solution()
print sol.arrayPairSum([1, 4, 3, 2])	
