class Solution(object):
	def wiggleSort(self, nums):
		for i in range(1, len(nums)):
			if (i%2 == 0) ^ (nums[i-1]> nums[i]):
				nums[i-1], nums[i] = nums[i], nums[i-1]
		return nums
	
nums = [3, 5, 2, 1, 6, 4]
sol = Solution()
print sol.wiggleSort(nums)

