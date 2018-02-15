class Solution():
	def threeSumSmaller(self, nums, target):
		nums = sorted(nums)
		ret = 0
		for i in range(0, len(nums) - 2):
			low = i + 1
			high = len(nums) - 1
			while low < high:
				if nums[i] + nums[low] + nums[high] < target:
					ret += high - low
					low += 1
				else:
					high -= 1
		return ret

sol = Solution()
nums = [-2, 0, 1, 3]
target = 2
print sol.threeSumSmaller(nums, target)
