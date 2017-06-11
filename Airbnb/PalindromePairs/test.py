class Solution(object):
	def palindromePairs(self, words):
		dict = {}
		res = []
		for i in range(len(words)):
			dict[words[i]] = i
		for i in range(len(words)):
			for j in range(len(words[i])):
				left = words[i][:j]
				right = words[i][j:]
				if self.isPalindrome(left):
					right_rev = right[::-1]
					if right_rev in dict and dict[right_rev]!= i:
						res.append([dict[right_rev], i])
				if self.isPalindrome(right):
					left_rev = left[::-1]
					if left_rev in dict and dict[left_rev] != i:
						res.append([i, dict[left_rev]])
		return res

	def isPalindrome(self, word):
		i = 0
		j = len(word) - 1
		while i < j:
			if word[i]!=word[j]:
				return False
			i += 1
			j -= 1
		return True

sol = Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
print sol.palindromePairs(words)
