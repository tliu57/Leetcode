class Solution(object):
	def search(self, nums, target):
		if not nums or len(nums) == 0:
			return -1
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = (low + high) / 2
			if nums[mid] == target:
				return mid
			elif nums[mid] > nums[high]:
				if target < nums[mid] and target >= nums[low]:
					high = mid - 1
				else:
					low = mid + 1
			elif nums[mid] < nums[high]:
				if target > nums[mid] and target <= nums[high]:
					low = mid + 1
				else:
					high = mid - 1
			else:
				high -= 1
		if nums[low] == target:
			return low
		else:
			return -1

sol = Solution()
print sol.search([4, 5, 6, 7, 0, 1, 2], 0)
print sol.search([1, 3], 3)
