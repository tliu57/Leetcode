class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.Word = False

class Trie(object):
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for c in word:
			if not c in curr.children:
				curr.children[c] = TrieNode()
			curr = curr.children[c]
		curr.Word = True

	def search(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children:
				return False
			curr = curr.children[c]
		return curr.Word

	def startsWith(self, prefix):
		curr = self.root
                for c in prefix:
		        if c not in curr.children:
				return False
			curr = curr.children[c]
		return True

obj = Trie()
obj.insert("Test")
print obj.search("Test")
print obj.search("Testt")
print obj.startsWith("Te")

