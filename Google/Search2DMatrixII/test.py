
class Solution():
	def searchMatrix(self, matrix, target):
		count = 0
		if not matrix:
			return count
		m = len(matrix)
		n = len(matrix[0])
		i = m - 1
		j = 0
		while i >= 0 and j < n:
			if matrix[i][j] == target:
				count += 1
				i -= 1
				j += 1
			elif matrix[i][j] < target:
				j += 1
			else:
				i -= 1
		return count

matrix = [
		[1, 3, 5, 7],
		[2, 4, 7, 8],
		[3, 5, 9, 10]
	]

sol = Solution()
print sol.searchMatrix(matrix, 3)
