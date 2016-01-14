class Solution(object):
	def isValid(self, s):
		stack = ['0']
		for c in s:
			if c != stack[-1] and abs(ord(c) - ord(stack[-1])) < 3:
				stack.pop()
			else:
				stack.append(c)
			print stack
		return stack==['0']

sol = Solution()
s = "()"
print sol.isValid(s)
