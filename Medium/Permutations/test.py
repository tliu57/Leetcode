class Solution(object):
	def permute(self, nums):
		ret = []
		if not nums:
			return ret
		self.permuteHelper([], nums, ret)
		return ret

	def permuteHelper(self, sub, nums, res):
		if len(sub) == len(nums):
			 res.append([elem for elem in sub])
		else:
			for i in range(len(nums)):
				if nums[i] in sub:
					continue
				sub.append(nums[i])
				self.permuteHelper(sub, nums, res)
				sub.pop()

sol = Solution()
print sol.permute([1, 2, 3])
