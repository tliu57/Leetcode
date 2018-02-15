import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
	result = []
	if not nums1 or not nums2:
		return result
	heap = []
	def push(i, j):
	    if i < len(nums1) and j < len(nums2):
		heapq.heappush(heap, [nums1[i] + nums2[j], i, j])
	
	push(0, 0)
	while heap and len(result) < k:
		_ , i, j = heapq.heappop(heap)
		result.append([nums1[i], nums2[j]])
		push(i, j+1)
		if j == len(nums2):
		    	i += 1
			j = 0
			push(i, j)
	return result

sol = Solution()
print sol.kSmallestPairs([1,1,2], [1, 2, 3], 2)
		
