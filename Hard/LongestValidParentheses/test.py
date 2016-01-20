class Solution(object):
	def longestValidParentheses(self, s):
		if not s:
			return 0
		pos = range(1, len(s) + 1)
		res = 0

		for i in range(1, len(s)):
			j = pos[i - 1] - 1
			print "i is:", i
			print "j is:", j
			if s[i] == ")" and j>=0 and s[j] == "(":
				previous_start = pos[j - 1]
				print "previous start is", previous_start
				if previous_start <= j - 1:
					pos[i] = previous_start
				else:
					pos[i] = j
			print "pos[i] is", pos[i]
			res = max(res, i - pos[i] + 1)
		return res

s = "()"
sol = Solution()
print sol.longestValidParentheses(s)
