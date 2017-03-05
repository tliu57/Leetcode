class Solution(object):
	def threeSum(self, nums):
		nums.sort()
		res = []
		if len(nums) < 3:
			return res
		for i in range(len(nums)-2):
			if i == 0 or (i > 0 and nums[i] != nums[i-1]):
				low = i + 1
				high = len(nums) - 1
				while low < high:
					if nums[low] + nums[high] == 0 - nums[i]:
						res.append([nums[i], nums[low], nums[high]])
						while low < high and nums[low] == nums[low+1]:
							low += 1
						while low < high and nums[high] == nums[high - 1]:
							high -= 1
						low += 1
						high -= 1
					elif nums[low] + nums[high] < -nums[i]:
						low += 1
					elif nums[low] + nums[high] > -nums[i]:
						high -= 1
		return res

sol = Solution()
print sol.threeSum([-1, 0, 1, 2, -1, -4])

