class Solution(object):
	def __init__(self):
		self.dp = []

	def combinationSum4(self, nums, target):
		self.dp = [-1 for i in range(target+1)]
		if not nums or len(nums) == 0:
			return 0
		self.dp[0] = 1
		res = self.combinationSum4Helper(nums, target)
		return res

	def combinationSum4Helper(self, nums, target):
		if self.dp and self.dp[target] != -1:
			return self.dp[target]
		res = 0
		for num in nums:
			if target - num >= 0:
				res += self.combinationSum4Helper(nums, target - num)
		self.dp[target] = res
		return self.dp[target]

sol = Solution()
print sol.combinationSum4([1, 2, 3], 4)
