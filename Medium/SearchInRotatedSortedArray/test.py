class Solution(object):
	def search(self, nums, target):
		if not nums or len(nums) == 0:
			return -1
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = (low + high) / 2
			if nums[mid] > nums[high]:
				low = mid + 1	
			else:
				high = mid
		pivot = low
		
		if nums[0] == target:
			return 0
		if nums[0] > target or pivot == 0:
			return self.binarySearch(pivot, len(nums) - 1, nums, target)
		else:
			return self.binarySearch(0, pivot-1, nums, target)

	def binarySearch(self, low, high, nums, target):
		left = low
		right = high
		if target < nums[left] or target > nums[right] or left > right:
			return -1
		while left < right:
			mid = (left+right) / 2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				right = mid - 1
			else:
				left = mid + 1
		if nums[left] == target:
			return left
		else:
			return -1

sol = Solution()
print sol.search([4, 5, 6, 7, 0, 1, 2], 5)
			
