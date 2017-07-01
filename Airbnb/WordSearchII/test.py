class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.word = False

class Trie(object):
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for c in word:
			if not c in curr.children:
				curr.children[c] = TrieNode()
			curr = curr.children[c]
		curr.word = True

	def search(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children:
				return False
			curr = curr.children[c]
		return curr.word

class Solution(object):
	def buildTrie(self, words):
		trie = Trie()
		for word in words:
			trie.insert(word)
		return trie.root

	def findWords(self, board, words):
		res= []
		root = self.buildTrie(words)
		m = len(board)
		n = len(board[0])
		for i in range(m):
			for j in range(n):
				self.dfs(board, i, j, "", root, res)
		return res

	def dfs(self, board, i, j, path, node, res):
		c = board[i][j]
		if c == '#' or c not in node.children:
			return
		path += c
		node = node.children[c]
		if node.word:
			res.append(path)
		board[i][j] = "#"
		if i > 0:
			self.dfs(board, i-1, j, path, node, res)
		if j > 0:
			self.dfs(board, i, j-1, path, node, res)
		if i < len(board) - 1:
			self.dfs(board, i+1, j, path, node, res)
		if j < len(board[0]) - 1:
			self.dfs(board, i, j+1, path, node, res)
		board[i][j] = c



sol = Solution()
words = ["oath", "pea", "eat", "rain"]
board = [
	 [ 'o', 'a', 'a', 'n'],
	 [ 'e', 't', 'a', 'e'],
	 [ 'i', 'h', 'k', 'r'],
	 [ 'i', 'f', 'l', 'v']
	]
print sol.findWords(board, words)
