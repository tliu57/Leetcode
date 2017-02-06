class Solution(object):
	def multiply(self, A, B):
		if not A or not B:
			return None
		m = len(A)
		n = len(A[0])
		nB = len(B[0])
		res = [[0 for i in range(nB)] for j in range(m)]
		for i in range(m):
			for k in range(n):
				if A[i][k] != 0:
					for j in range(nB):
						if B[k][j] != 0:
							res[i][j] += A[i][k] * B[k][j]
		return res

sol = Solution()
A = [
	[1, 0, 0],
	[-1, 0, 3]
]

B = [
	[7, 0, 0],
	[0, 0, 0],
	[0, 0, 1]
] 
print sol.multiply(A, B)

