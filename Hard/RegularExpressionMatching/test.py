class Solution(object):
	def isMatch(self, s, p):
		m = len(s)
		n = len(p)
		matrix = [[False for i in range(n+1)] for j in range(m+1)]
		
		matrix[0][0] = True
		for i in range(1, m+1):
			matrix[i][0] = False
		for j in range(n+1):
			if j > 1:
				matrix[0][j] = (p[j-1] == '*') and (matrix[0][j-2])
		for i in range(1, m+1):
			for j in range(1, n+1):
				if p[j-1] == '*':
					matrix[i][j] = matrix[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and matrix[i-1][j]) 
				else:
					matrix[i][j] = matrix[i-1][j-1] and (p[j-1] == '.' or s[i-1] == p[j-1])
		return matrix[m][n]	


sol = Solution()

print sol.isMatch("aa", "a")
print sol.isMatch("aa", "aa")
print sol.isMatch("aaa", "aa")
print sol.isMatch("aa", "a*")
print sol.isMatch("aa", ".*")
print sol.isMatch("ab", ".*")
print sol.isMatch("aab", "c*a*b")
