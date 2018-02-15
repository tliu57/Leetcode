class Solution(object):
	def moveZeros(self, nums):
		count = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				count += 1
			else:
				nums[i - count] = nums[i]
		for i in range(len(nums)-count, len(nums)):
			nums[i] = 0
nums = [0, 1, 0, 3, 12]
sol = Solution()
sol.moveZeros(nums)
print nums
