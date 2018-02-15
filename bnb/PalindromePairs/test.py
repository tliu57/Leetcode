class Solution(object):
	def palindromePairs(self, words):
		dict = {}
		res = []
		for i in range(len(words)):
			dict[words[i]] = i
		for i in range(len(words)):
			for j in range(len(words[i])+1):
				left = words[i][:j]
				right = words[i][j:]
				right_rev = right[::-1]
				left_rev = left[::-1]
				if left_rev in dict and dict[left_rev]!= i and right == right[::-1]:
					res.append([i, dict[left_rev]])
				if j > 0 and right_rev in dict and dict[right_rev] != i and left == left[::-1]:
					res.append([dict[right_rev], i])
		return res


sol = Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
corner = ["a", ""]
print sol.palindromePairs(words)

