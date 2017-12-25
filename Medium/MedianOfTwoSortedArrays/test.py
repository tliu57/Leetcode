import sys
class Solution(object):
    def findMedianSortedArrays(self, A, B):
	m = len(A)
	n = len(B)
	if (m+n)%2 == 1:
	    return self.helper(A, 0, B, 0, (m+n)/2 + 1)
	else:
	    return float(self.helper(A, 0, B, 0, (m+n)/2) + self.helper(A, 0, B, 0, (m+n)/2 + 1))/2.0

    def helper(self, arrayA, A_start, arrayB, B_start, k):
	m = len(arrayA)
	n = len(arrayB)
	if A_start >= m:
		return arrayB[B_start + k - 1]
	if B_start >= n:
		return arrayA[A_start + k - 1]
	if k == 1:
		return min(arrayA[A_start], arrayB[B_start])
	A_key = arrayA[A_start + k/2 - 1] if A_start + k/2-1 < m else sys.maxint
	B_key = arrayB[B_start + k/2 - 1] if B_start + k/2-1 < n else sys.maxint
	if A_key < B_key:
		return self.helper(arrayA, A_start + k/2, arrayB, B_start, k - k/2)
	else:
	    	return self.helper(arrayA, A_start, arrayB, B_start + k/2, k - k/2)

sol = Solution()
A = [1, 9, 10, 12, 13]
B = [4, 5, 6]
print sol.findMedianSortedArrays(A, B)
nums1 = [2, 3, 4, 5, 6]
nums2 = [1]
print sol.findMedianSortedArrays(nums1, nums2)
