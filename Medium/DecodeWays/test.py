class Solution(object):
	def numDecodings(self, s):
		if not s or len(s) == 0:
			return 0
		n = len(s)
		res = [0 for i in range(n+1)]
		res[n] = 1
		if s[n-1] == '0':
			res[n-1] = 0
		else:
			res[n-1] = 1
		for i in range(n-2, -1, -1):
			if s[i] == '0':
				continue
			elif int(s[i: i+2]) <= 26:
				res[i] = res[i+1] + res[i+2]
			else:
				res[i] = res[i+1]
		return res[0]

sol = Solution()
print sol.numDecodings("12")
print sol.numDecodings("10")
print sol.numDecodings("101")
