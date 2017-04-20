class Solution(object):
	def findMin(self, nums):
		if not nums:
			return None
		lo = 0
		hi = len(nums) - 1
		while lo < hi:
			mid = lo + (hi - lo)/2
			if nums[mid] > nums[hi]:
				lo = mid + 1
			elif nums[mid] < nums[hi]:
				hi = mid
			else:
				hi = hi - 1
		return nums[lo]

sol = Solution()
print sol.findMin([4, 5, 0, 1, 3, 3, 4])
