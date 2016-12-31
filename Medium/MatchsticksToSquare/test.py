class Solution(object):
	def makesquare(self, nums):
		if not nums or len(nums) < 4:
			return False
		numsum = sum(nums)
		if not numsum % 4 == 0:
			return False
		nums = sorted(nums, reverse=True)
		return self.dfs(nums, [0]*4, 0, numsum/4)

	def dfs(self, nums, sums, index, target):
		if index == len(nums):
			if sums[0] == target and sums[1] == target and sums[2] == target:
				return True
			return False
		for i in range(4):
			if sums[i] + nums[index] > target:
				continue
			sums[i] += nums[index]
			if self.dfs(nums, sums, index + 1, target):
				return True
			sum[i] -= nums[index]

		return False

		
sol = Solution()
nums = [1, 1, 2, 2, 2]
print sol.makesquare(nums)
