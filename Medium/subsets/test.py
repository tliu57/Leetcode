class Solution(object):
	def subsets(self, nums):
		ret = []
		if not nums:
			return ret
		nums.sort()
		self.subsetsHelper(0, [], nums, ret)
		return ret

	def subsetsHelper(self, pos, sub_list, nums, ret):
		ret.append([num for num in sub_list])
		for i in range(pos, len(nums)):
			sub_list.append(nums[i])
			self.subsetsHelper(i+1, sub_list, nums, ret)
			sub_list.pop()

sol = Solution()
print sol.subsets([1, 2, 3])
		
