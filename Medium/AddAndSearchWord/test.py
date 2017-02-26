class TrieNode():
	def __init__(self):
		self.children = {}
		self.Word = False

class WordDictionary(object):
	def __init__(self):
		self.root = TrieNode()
	
	def addWord(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
		node.Word = True		

	def search(self, word):
		node = self.root
		self.res = False
		self.dfs(node, word)
		return self.res

	def dfs(self, node, word):
		if not word:
			if node.Word:
				self.res = True
			return
		elif word[0] == '.':
			for n in node.children.values():
				self.dfs(n, word[1:])
		else:
			node = node.children.get(word[0])
			if not node:
				return
			self.dfs(node, word[1:])


obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print obj.search("pad")
print obj.search("bad")
print obj.search(".ad")
print obj.search("b..")
