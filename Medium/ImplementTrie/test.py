class TrieNode(object):
	def __init__(self):
		self.node = defaultDict(TrieNode)
		self.isWord = False

class Trie(object):
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for c in word:
			curr = curr.node[c]
		curr.isWord = True

	def search(self, word):
		curr = self.root
		for c in word:
			if c not in curr.nodes:
				return False
			curr = curr.nodes[c]
		return curr.isWord

	def startsWith(self, prefix):
		curr = self.root
                for c in word:
		        if c not in curr.nodes:
				return False
			curr = curr.nodes[c]
		return True
