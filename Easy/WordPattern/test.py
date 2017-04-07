class Solution(object):
	def wordPattern(self, pattern, str):
		s = pattern
		t = str.split()
		return [s.index(elem) for elem in s] == [t.index(elem) for elem in t]

sol = Solution()
print sol.wordPattern("abba", "cat dog dog cat")
