class Solution(object):
	def __init__(self):
		self.dp = None

	def combinationSum4(self, nums, target):
		self.dp = [-1 for i in range(target+1)]
		if not nums or len(nums) == 0:
			return 0
		self.dp[0] = 1
		res = self.helper(nums, target)
		return res

	def helper(self, nums, target):
		if self.dp and self.dp[target] != -1:
			return self.dp[target]
		res = 0
		for num in nums:
			if target >= num:
				res += self.helper(nums, target - num)
		self.dp[target] = res
		return res

sol = Solution()
nums = [1, 2, 3]
target = 4
print sol.combinationSum4(nums, target) 
		
