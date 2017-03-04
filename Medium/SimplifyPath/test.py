class Solution(object):
	def simplifyPath(self, path):
		array = [elem for elem in path.split("/") if elem != '.' and elem != '']
		stack = []
		for c in array:
			if c == "..":
				if len(stack) > 0:
					stack.pop()
			else:
				stack.append(c)
		return "/" + "/".join(stack)

sol = Solution()
print sol.simplifyPath("/home/")
print sol.simplifyPath("/a/./b/../../c/")

test_stack = ["abc", "abd", "bcd"]
print "/".join(test_stack)
