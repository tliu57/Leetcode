class Solution(object):
    def numDecodings(self, s):
	if not s:
		return 0
	n = len(s)
	mod = 1000000007
	dp = [0 for i in range(n+1)]
	dp[0] = 1
	for i in range(1, len(dp)):
		if s[i-1] == "*":
	    		dp[i] = (dp[i] + 9*dp[i-1]) % mod
	 		if i > 1:
	 			if s[i-2] == "*":
	 				dp[i] = (dp[i] + 15 * dp[i-2]) % mod
	 			elif s[i-2] == '1':
	 				dp[i] = (dp[i] + 9*dp[i-2]) % mod
	 			elif s[i-2] == '2':
	 				dp[i] = (dp[i] + 6*dp[i-2]) % mod
		else:
			if s[i-1] > "0" and s[i-1] <= '9':
				dp[i] = (dp[i] + dp[i-1]) % mod
			if i > 1:
				if s[i-2] == "*":
					if s[i-1] >= '0' and s[i-1] <= '6':
						dp[i] = (dp[i] + 2 * dp[i-2]) % mod
					elif s[i-1] >= '7' and s[i-1] <= '9':
						dp[i] = (dp[i] + dp[i-2]) % mod
				else:
					twoDigits = int(s[i-2:i])
					if twoDigits >= 10 and twoDigits <= 26:
						dp[i] = (dp[i] + dp[i-2]) % mod
	return dp[n]

sol = Solution()
print sol.numDecodings("1*")
print sol.numDecodings("**")
