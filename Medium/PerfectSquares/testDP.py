import sys

class Solution(object):
	def numSquares(self, n):
		if n <= 0:
			return 0
		numSquareCnt = [sys.maxint] * (n+1)
		numSquareCnt[0] = 0

		for i in range(1, n+1):
			j = 1
			while j*j <= i:
				numSquareCnt[i] = min(numSquareCnt[i], numSquareCnt[i - j*j] + 1)
				j += 1
		print numSquareCnt
		return numSquareCnt.pop()

sol = Solution()
print sol.numSquares(12)
