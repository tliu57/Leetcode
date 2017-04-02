class Solution(object):
	def removeDuplicates(self, nums):
		if len(nums) < 2:
			return nums
		curr = 1
		for idx in range(1, len(nums)):
			if nums[idx] != nums[idx - 1]:
				nums[curr] = nums[idx]
				curr += 1
		return curr
sol = Solution()
nums = [1, 1, 2]
print sol.removeDuplicates(nums)
