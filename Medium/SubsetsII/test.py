class Solution(object):
	def subsetsWithDup(self, nums):
		ret = []
		if not nums:
			return ret
		nums.sort()
		self.subsetsHelper(0, [], nums, ret)
		return ret

	def subsetsHelper(self, pos, sublist, nums, ret):
		ret.append([num for num in sublist])
		for i in range(pos, len(nums)):
			if i > pos and nums[i] == nums[i-1]:
				continue
			sublist.append(nums[i])
			self.subsetsHelper(i+1, sublist, nums, ret)
			sublist.pop()


sol = Solution()
print sol.subsetsWithDup([1, 2, 2])
