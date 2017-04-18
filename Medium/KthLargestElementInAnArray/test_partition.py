class Solution(object):
	def findKthLargest(self, nums, k):
		pos = self.partition(nums, 0, len(nums)-1)
		if len(nums) - pos < k:
			return self.findKthLargest(nums[:pos], k-(len(nums) - pos))
		elif len(nums) - pos > k:
			return self.findKthLargest(nums[pos+1:], k)
		else:
			return nums[pos]

	def partition(self, nums, l, r):
		pivot = nums[r]
		lo = l
		for i in range(l, r):
			if nums[i] < pivot:
				nums[i], nums[lo] = nums[lo], nums[i]
				lo += 1
		nums[lo], nums[r] = nums[r], nums[lo]
		return lo

sol = Solution()
print sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
