class Solution(object):
	def removeInvalidParentheses(self, s):
		ans = list()
		self.removeInvalidParenthesesHelper(s, ans, 0, 0, ('(', ')'))
		return ans

	def removeInvalidParenthesesHelper(self, s, ans_list, last_i, last_j, pair):
		counter = 0
		for i in range(last_i, len(s)):
			if s[i] == pair[0]:
				counter += 1
			if s[i] == pair[1]:
				counter -= 1
			if counter >= 0:
				continue
			for j in xrange(last_j, i+1):
				if s[j] == pair[1] and (j == last_j or s[j-1] != pair[1]):
					self.removeInvalidParenthesesHelper(s[:j]+s[j+1:], ans_list, i, j, pair)
			return
		reversed = s[::-1]
		if pair[0] == '(':
			self.removeInvalidParenthesesHelper(reversed, ans_list, 0, 0, (')', '('))
		else:
			ans_list.append(s)


sol = Solution()
s = "()())()"
print sol.removeInvalidParentheses(s)
			
