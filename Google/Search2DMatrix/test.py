
class Solution:
	def searchMatrix(self, matrix, target):
		if not matrix:
			return False
		m = len(matrix)
		n = len(matrix[0])
		iBegin = 0
		iEnd = m - 1
		while iBegin+1 < iEnd:
			iMid = iBegin + (iEnd - iBegin)/2
			if matrix[iMid][0] == target:
				return True
			elif matrix[iMid][0] > target:
				iEnd = iMid
			else:
				iBegin = iMid
		if matrix[iEnd][0] <= target:
			row = iEnd
		elif matrix[iBegin][0] <= target:
			row = iBegin
		else:
			return False		

		jBegin = 0
		jEnd = n - 1
		while jBegin+1 < jEnd:
			jMid = jBegin + (jEnd - jBegin)/2
			if matrix[row][jMid] == target:
				return True
			elif matrix[row][jMid] > target:
				jEnd = jMid
			else:
				jBegin = jMid
		if matrix[row][jEnd] == target:
			return True
		elif matrix[row][jBegin] == target:
			return True
		else:
			return False


matrix = [
	  [1, 3, 5, 7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
sol = Solution()
print sol.searchMatrix(matrix, 3)
