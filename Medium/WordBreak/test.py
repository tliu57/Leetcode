class Solution(object):
	def wordBreak(self, s, wordDict):
		dp = [0 for i in range(len(s)+1)]
		dp[0] = 1 
		for i in range(1, len(s)+1):
			for j in range(0, i):
				dp[i] = dp[j] and (s[j:i] in wordDict)
				if dp[i]:
					break
		return dp[len(s)]

sol = Solution()
print sol.wordBreak("leetcode", ["leet", "code"])


