class Solution(object):
	def __init__(self):
		self.kvmap = {
				"2": "abc",
				"3": "def",
				"4": "ghi",
				"5": "jkl",
				"6": "mno",
				"7": "pqrs",
				"8": "tuv",
				"9": "wxyz"
			     }

	def letterCombinations(self, digits):
		out = []
		if not digits:
			return out
		offset = 0
		self.dfs("", digits, offset, out)
		return out

	def dfs(self, prefix, digits, offset, out):
		if offset == len(digits):
			out.append(prefix)
			return
		currVal = self.kvmap[digits[offset]]
		for val in currVal:
			self.dfs(prefix+val, digits, offset+1, out)

sol = Solution()
# print sol.letterCombinations("23")
print sol.letterCombinations("")

