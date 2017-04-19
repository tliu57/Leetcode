class Solution(object):
	def findMin(self, nums):
		if not nums:
			return None
		i = 0
		j = len(nums)-1
		while i < j:
			if nums[i] < nums[j]:
				j -= 1
			else:
				i += 1
		return nums[i]

sol = Solution()
print sol.findMin([4, 5, 6, 7, 0, 1, 2])
