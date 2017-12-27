class Node(object):
    def __init__(self):
	self.children = {}
	self.end = 0
	self.word = ""

class Trie(object):
    def __init__(self):
	self.root = Node()

    def insert(self, word, index):
	curr = self.root
	for c in word:
		if not c in curr.children:
    			curr.children[c] = Node()
		curr = curr.children.get(c)
	curr.end = index
	curr.word = word

    def dfs(self, words):
	ans = ""
	stack = []
	stack.append(self.root)
	while stack:
	    node = stack.pop()
	    if node.end > 0 or node == self.root:
	    	if node != self.root > 0:
			word = words[node.end - 1]
			if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
			    ans = word
	    	for n in node.children.values():
		    stack.append(n)
	return ans

class Solution(object):
    def longestWord(self, words):
	root = Trie()
	index = 1
	for word in words:
	    root.insert(word, index)
	    index += 1
	return root.dfs(words)

sol = Solution()
print sol.longestWord(["w","wo","wor","worl", "world"])

