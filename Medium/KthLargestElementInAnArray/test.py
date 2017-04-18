import heapq
class Solution(object):
	def findKthLargest(self, nums, k):
		heap = nums[:k]
		heapq.heapify(heap)
		for num in nums[k:]:
			if num > heap[0]:
				heapq.heapreplace(heap, num)
		return heap[0]	
sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print sol.findKthLargest(nums, k)
