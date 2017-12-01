class Solution(object):
    def kthSmallest(self, matrix, k):
	m = len(matrix)
	if m < 1:
		return 0
	n = len(matrix[0])
	lo = matrix[0][0]
	hi = matrix[m-1][n-1] + 1
	while lo < hi:
		mid = lo + (hi - lo)/2
		count = 0
		j = n-1
		for i in range(0, m):
			while j >= 0 and matrix[i][j] > mid:
				j -= 1
			count += (j+1)
		if count < k:
		 	lo = mid + 1
		else:
		 	hi = mid
	return lo

sol = Solution()
matrix = [
	  [1, 5, 9],
	  [10, 11, 13],
	  [12, 13, 15]
]
print sol.kthSmallest(matrix, 8)
