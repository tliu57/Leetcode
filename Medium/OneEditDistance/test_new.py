class Solution(object):
	def isOneEditDistance(self, s, t):
		for i in range(min(len(s), len(t))):
			if s[i] != t[i]:
				if len(s) == len(t):
					return s[i+1:] == t[i+1:]
				elif len(s) < len(t):
					return s[i:] == t[i+1:]
				else:
					return s[i+1:] == t[i:]
		return abs(len(s) - len(t)) == 1

sol = Solution()
s = "abc"
t = "abd"
# print sol.isOneEditDistance(s, t)

# print s[4:]

s1 = "abcd"
t1 = "abd"
# print sol.isOneEditDistance(s1, t1)

s2 = "abd"
t2 = "abce"
# print sol.isOneEditDistance(s2, t2)

s3 = "ab"
t3 = "cab"
print sol.isOneEditDistance(s3, t3)
