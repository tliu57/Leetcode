class Solution(object):
	def dfs(self, curr, skips, vis, remains):
		if remains == 0:
			return 1
		if remains < 0:
			return 0
		vis[curr] = True
		res = 0
		for i in range(1, 10):
			if vis[i] == False and (skips[curr][i] == 0 or vis[skips[curr][i]] == True):
				res += self.dfs(i, skips, vis, remains - 1)
		vis[curr] = False
		return res

	def numberOfPatterns(self, m, n):
		skips = [[0 for i in range(10)] for j in range(10)]
		skips[1][3] = skips[3][1] = 2
		skips[1][7] = skips[7][1] = 4
		skips[3][9] = skips[9][3] = 6
		skips[7][9] = skips[9][7] = 8
		skips[1][9] = skips[9][1] = skips[2][8] = skips[8][2] = skips[3][7] = skips[7][3] = skips[4][6] = skips[6][4] = 5
		visited = [False for i in range(1, 11)]
		result = 0
		for i in range(m, n+1):
			result += self.dfs(1, skips, visited, i-1) * 4
			result += self.dfs(2, skips, visited, i-1) * 4
			result += self.dfs(5, skips, visited, i-1)
		return result

sol = Solution()
print sol.numberOfPatterns(3, 4) 
