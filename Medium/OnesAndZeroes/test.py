class Solution():
	def findMaxForm(self, strs, m, n):
		dp = [[0 for x in range(n+1)] for y in range(m+1)]
		for s in strs:
			count = self.count(s)
			for i in range(m, count[0]-1, -1):
				for j in range(n, count[1]-1, -1):
					dp[i][j] = max(1 + dp[i-count[0]][j-count[1]], dp[i][j])
		print dp
		return dp[m][n]

	def count(self, str):
		OneZeroes = [0 for x in range(2)]
		for character in str:
			OneZeroes[ord(character) - ord('0')] += 1
		return OneZeroes

sol = Solution()
test_arr1 = ["10", "0001", "111001", "1", "0"]
test_arr2 = ["10", "0", "1"]
print sol.findMaxForm(test_arr1, 5, 3)
print sol.findMaxForm(test_arr2, 1, 1)

