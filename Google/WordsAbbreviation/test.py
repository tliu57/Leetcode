class Solution(object):
	def getUniqueAbbreviation(self, words):
		n = len(words)
		prefix = [1 for i in range(n)]
		ans = ["" for i in range(n)]
		map = {}
		for i in range(n):
			ans[i] = self.getAbbr(words[i], 1)
			map[ans[i]] = map.get(ans[i], 0) + 1
		while True:
			isUnique = True
			for i in range(n):
				if map[ans[i]] > 1:
					isUnique = False
					prefix[i] += 1
					ans[i] = self.getAbbr(words[i], prefix[i])
					map[ans[i]] = map.get(ans[i], 0) + 1
			if isUnique:
				break
		return ans
	

	def getAbbr(self, word, index):
		if not word or len(word) <= 2:
			return word
		if index >= len(word) - 2:
			return word
		ans = word[:index] + str(len(word)-1-index) + word[-1]
		return ans



words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
sol = Solution()
print sol.getUniqueAbbreviation(words)
