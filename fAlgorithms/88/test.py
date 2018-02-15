class Solution(object):
	def merge(self, nums1, m, nums2, n):
		A = [0 for i in range(m + n)]
		while m > 0 and n > 0:
			if nums1[m-1] >= nums2[n-1]:
				A[m+n-1] = nums1[m-1]
				m -= 1
			else:
				A[m+n-1] = nums2[n-1]
				n -= 1
		if n > 0:
			A[:n] = nums2[:n]
		else:
			A[:m] = nums1[:m]
		return A

sol = Solution()
print sol.merge([1, 2, 3], 3, [3, 4], 2)
