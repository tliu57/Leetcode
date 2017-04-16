class Solution(object):
	def sortColors(self, nums):
		if not nums or len(nums) == 1:
			return nums
		r = 0
		b = len(nums) - 1
		for i in range(b + 1):
			while nums[i] == 2 and i < b:
				nums[i], nums[b] = nums[b], nums[i]
				b -= 1
			while nums[i] == 0 and i > r:
				nums[i], nums[r] = nums[r], nums[i]
				r += 1
		return nums

sol = Solution()
# print sol.sortColors([0, 1, 2, 0, 1, 2])
# print sol.sortColors([0, 0])
# print sol.sortColors([2, 2])
print sol.sortColors([1, 0])
