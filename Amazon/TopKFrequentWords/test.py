class Node(object):
    def __init__(self):
	self.children = {}
	self.word = None
	self.isWord = False

class Solution(object):
    def addWord(self, count, i, word):
	curr = count[i]
	for c in word:
		curr.children[c]= Node()
		curr = curr.children.get(c)
	curr.word = word
	curr.isWord = True
	
    def getWord(self, ans, node, k):
	if not node:
		return
	if node.isWord:
		ans.append(node.word)
	if len(ans) == k:
		return
	curr = node
	for c in curr.children:
		self.getWord(ans, curr.children.get(c), k)

    def topKFrequent(self, words, k):
	freqMap = {}
	for word in words:
		if word not in freqMap:
			freqMap[word] = 0
		freqMap[word] += 1
	
	count = [Node() for i in range(len(words))]
	for key in freqMap.keys():
	    keyFreq = freqMap[key]
	    self.addWord(count, keyFreq, key)
	
	ans = []
	for i in range(len(count)-1, 0, -1):
		if count[i]:
			self.getWord(ans, count[i], k)
			if len(ans) == k:
				break
	return ans

sol = Solution()
# print sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
print sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
