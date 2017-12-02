class Solution():
    def findLeftMostOne(self, matrix):
	m = len(matrix)
	n = len(matrix[0])
	mid = n/2
	left = mid
	i = 1
	while matrix[0][left] == 0:
		left += 1
	while i < m and left >= 0 and left < n:
		while matrix[i][left] == 1:
			left -= 1
		left += 1
		if left == 0:
			return 0
		else:
			i += 1
	return left

matrix = [
	  [0, 0, 0, 1, 1],
	  [0, 0, 0, 1, 1],
	  [0, 0, 0, 1, 1],
	  [0, 1, 1, 1, 1]
]

sol = Solution()
print sol.findLeftMostOne(matrix)
