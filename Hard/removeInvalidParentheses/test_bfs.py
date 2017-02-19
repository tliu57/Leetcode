from collections import deque
from sets import Set

class Solution(object):
	def removeInvalidParentheses(self, s):
		ans = []
		visited = Set()
		visited.add(s)
		queue = deque()
		queue.append(s)
		while queue:
			curr_str = queue.popleft()
			curr_imb_brac =  self.findImbalancedBrackets(curr_str) 
			if curr_imb_brac == 0 and curr_str not in ans:
				ans.append(curr_str)
			else: 
				for i in range(len(curr_str)):
					if curr_str[i] not in ('(', ')'):
						continue
					new_str = curr_str[:i] + curr_str[i+1:]
					if new_str not in visited and self.findImbalancedBrackets(new_str) < curr_imb_brac:
						queue.append(new_str)
		return ans

	def findImbalancedBrackets(self, string):
		left_brackets = 0
		right_brackets = 0
		for c in string:
			left_brackets += {"(":1, ")": -1}.get(c, 0)
			right_brackets += left_brackets < 0
			left_brackets = max(left_brackets, 0)
		return left_brackets + right_brackets
			

sol = Solution()
string1 = "()())()"
string2 = "(a)())()"
string3 = ")("
print sol.removeInvalidParentheses(string1)
print sol.removeInvalidParentheses(string2)
print sol.removeInvalidParentheses(string3)						

string4 = ")(((((((("
print sol.removeInvalidParentheses(string4)	
