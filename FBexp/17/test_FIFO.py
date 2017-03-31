class Solution(object):
	def letterCombinations(self, digits):
		mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		ans = [""]
		for i in range(len(digits)):
			while i == len(ans[-1]):
				t = ans.pop()
				for m in mapping[int(digits[i])]:
					ans.insert(0, t+m)
		return ans

sol = Solution()
print sol.letterCombinations("")
print sol.letterCombinations("23")
