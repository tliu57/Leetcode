class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.startsWith = []

class Trie(object):
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children:
				curr.children[c] = TrieNode()
			curr.children[c].startsWith.append(word)
			curr = curr.children[c]

	def findByPrefixes(self, prefix):
		ans = []
		curr = self.root
		for c in prefix:
			if c not in curr.children:
				return ans
			curr = curr.children[c]
		ans = [elem for elem in curr.startsWith]
		return ans

class Solution:
	def __init__(self):
		self.board = []
		self.depth = 0
		self.words = []
	
	def buildTrie(self, words):
		trieRoot = Trie()
		for w in words:
			trieRoot.insert(w)
		return trieRoot

	def wordSquares(self, words):
		if not words:
			return self.board
		self.words = words
		self.depth = len(words[0])
		root = self.buildTrie(words)
		self.dfs(0, [], root)
		return self.board

	def dfs(self, l, path, trieRoot):
		if l == self.depth:
			self.board.append([elem for elem in path])
			return

		prefix = ""
		if path:
			for i in range(l):
				prefix += path[i][l:l+1]
		remains = trieRoot.findByPrefixes(prefix)  
		if prefix == "":
			remains = self.words
		for w in remains:
			convertWord = str(w)
			path.append(convertWord)
			self.dfs(l+1, path, trieRoot)
			path.pop()

sol = Solution()
sequence = ["ball","area","lead","lady", "late"]
sequence1 = ["area","lead","wall","lady","ball"]
print (sol.wordSquares(sequence1))
# test_trie = Trie()
# for w in sequence:
# 	test_trie.insert(w)
	
# print (test_trie.findByPrefixes("la"))
