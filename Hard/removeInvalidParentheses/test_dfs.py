from sets import Set
class Solution(object):
	def removeInvalidParentheses(self, s):
		ans = []
		visited = Set()
		self.dfs(ans, visited, s)
		return ans

	def dfs(self, ans, visited, s):
		visited.add(s)
		curr_invalid_brac = self.find_inbalanced_bracket(s)
		if curr_invalid_brac == 0 and s not in ans:
			ans.append(s)
		for i in range(len(s)):
			new_s = s[:i] + s[i+1:]
			if new_s in visited:
				continue
			new_invalid_brac = self.find_inbalanced_bracket(new_s)
			if new_invalid_brac < curr_invalid_brac:
				self.dfs(ans, visited, new_s)
									

	def find_inbalanced_bracket(self, str):
		left_bracket = 0
		right_bracket = 0
		for c in str:
			left_bracket += {"(": 1, ")": -1}.get(c, 0)
			right_bracket += left_bracket < 0
			left_bracket = max(left_bracket, 0)
		return left_bracket+right_bracket

s1 = "()())()"
s2 = "(a)())()"
s3 = ")("
expected1 = ["()()()", "(())()"]
expected2 = ["(a)()()", "(a())()"]
expected3 = [""]

sol = Solution()
print sol.removeInvalidParentheses(s1)
print sol.removeInvalidParentheses(s2)
print sol.removeInvalidParentheses(s3)

s4 = ")(((((((("
print sol.removeInvalidParentheses(s4)
