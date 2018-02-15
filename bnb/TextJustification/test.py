class Solution(object):
	def fullJustify(self, words, maxWidth):
		res = []
		curr = []
		num_of_words = 0
		for w in words:
			if len(curr) + num_of_words + len(w) > maxWidth:
				for i in range(maxWidth - num_of_words):
					curr[i%(len(curr)-1 or 1)] += " "
				res.append(''.join(curr))
				curr = []
				num_of_words = 0
			curr.append(w)
			num_of_words += len(w)
		res.extend([' '.join(curr).ljust(maxWidth)])
		return res

sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print sol.fullJustify(words, maxWidth)

words2 = ["What", "must", "be", "shall", "be."]
maxWidth2 = 12
print sol.fullJustify(words2, maxWidth2)
