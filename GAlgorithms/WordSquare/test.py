class Solution:
	def __init__(self):
		self.board = []
		self.wordLen = 0		
		self.prefixes = {}

	def initPrefixes(self, words):
		for word in words:
			for i in range(len(word)):
				currPref = word[:i]
				if currPref not in self.prefixes:
					self.prefixes[currPref] = []
				self.prefixes[currPref].append(word)

	def wordSquares(self, words):
		path = []
		if not words:
			return self.board
		self.initPrefixes(words)
		self.wordLen = len(words[0])
		self.dfs(0, path)
		return self.board

	def dfs(self, l, path):
		if l == self.wordLen:
			self.board.append([elem for elem in path])
			return
		currPref = ""
		if path:
			for i in range(l):
				currPref += path[i][l:l+1]
		if currPref not in self.prefixes:
			return
		remains = self.prefixes[currPref]
		for word in remains:
			path.append(word)
			self.dfs(l+1,path)
			path.pop()

sol = Solution()
sequences = ["area","lead","wall","lady","ball"]
print (sol.wordSquares(sequences))
words = ["abat","baba","atan","atal"]
print (sol.wordSquares(words))
