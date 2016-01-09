class Solution(object):
	def canWin(self, s):
		flag = self.canWinHelper(s, False)
		return flag

	def canWinHelper(self, s, flag):
		for i in range(len(s)-1):
			if s[i:i+2] != "++":
				continue
			else:
				flag = flag or not self.canWinHelper(s[:i] + "--" + s[i+2:], flag)
		return flag

sol = Solution()
s = "++++"
print sol.canWin(s)
