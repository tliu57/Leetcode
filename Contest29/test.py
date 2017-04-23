class Solution(object):
	def longestLine(self, M):
		if not M:
			return 0
		m = len(M)
		n = len(M[0])
		max_len = 0
		for i in range(m):
			for j in range(n):
				if M[i][j] == 1:
					h_length = self.dfsHorizonal(M, i, j, 0)
					v_length = self.dfsVertical(M, i, j, 0)
					d_length = self.dfsDownRight(M, i, j, 0)
					l_length = self.dfsDownLeft(M, i, j, 0)
					max_len = max(max_len, h_length, v_length, d_length, l_length)
		return max_len

	def dfsHorizonal(self, M, i, j, length):
		if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]):
			return length
		if M[i][j] != 1:
			return length
		length += 1
		return self.dfsHorizonal(M, i+1, j, length)

	def dfsVertical(self, M, i, j, length):
		if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]):
			return length
		if M[i][j] != 1:
			return length
		length += 1
		return self.dfsVertical(M, i, j+1, length)

	def dfsDownRight(self, M, i, j, length):
		if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]):
			return length
		if M[i][j] != 1:
			return length
		length += 1
		return self.dfsDownRight(M, i+1, j+1, length)

	def dfsDownLeft(self, M, i, j, length):
		if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]):
			return length
		if M[i][j] != 1:
			return length
		length += 1
		return self.dfsDownLeft(M, i-1, j+1, length)


sol = Solution()
M = [[0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 1]]

M2 = [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]
print sol.longestLine(M2)
