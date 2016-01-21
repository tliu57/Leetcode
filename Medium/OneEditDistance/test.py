class Solution(object):
	def isOneEditDistance(self, s, t):
		if abs(len(s) - len(t)) > 1:
			return False
		if len(s) == len(t):
			return self.isOneEditReplacement(s, t)
		if len(s) == len(t) + 1:
		 	return self.isOneEditInsertion(s, t)
		else:
			return self.isOneEditInsertion(t, s)

	def isOneEditReplacement(self, s, t):
		i = 0
		while i < len(s) and s[i] == t[i]:
			i += 1
		diff_index = i - 1
		print "when break, i is:", i
		i += 1
		while i < len(s) and s[i] == t[i]:
			i += 1
		print "now i is:", i
		if i == len(s) :
			return True
		else:
			return False

	def isOneEditInsertion(self, long_str, short_str):
		if len(short_str) == 0:
			return True
		i = 0
		while i < len(short_str) and long_str[i] == short_str[i]:
			i += 1
		if i == len(short_str):
			return True
		while i < len(short_str) and long_str[i+1] == short_str[i]:
			i += 1
		return i == len(short_str)
sol = Solution()
s = "BA"
t = "A"
print sol.isOneEditDistance(s, t)
