class Solution(object):
    def __init__(self):
	self.result = []

    def buildPath(self, path, prevMap, start, word):
	if word == start:
		self.result.append([word] + path)
		return
	path.insert(0, word)
    	for w in prevMap[word]:
		self.buildPath(path, prevMap, start, w)
    	path.pop(0)

    def findLadders(self, beginWord, endWord, wordList):
	prevMap = {}
	wordSets = set()
    	wordSets.add(beginWord)
    	for word in wordList:
		wordSets.add(word)
	for word in wordSets:
		prevMap[word] = set()
	currLevel = set()
	currLevel.add(beginWord)
    	while True:
		prevLevel = currLevel
		currLevel = set()
		for word in prevLevel:
			wordSets.remove(word)
    		for currWord in prevLevel:
			for i in range(len(currWord)):
		    		part1 = currWord[:i]
		    		part2 = currWord[i+1:]
		    		for c in "abcdefghijklmnopqrstuvwxyz":
		    			newWord = part1 + c + part2
		    			if newWord != currWord and newWord in wordSets:
		    				prevMap[newWord].add(currWord)
		    				currLevel.add(newWord)
		if len(currLevel) == 0:
		      return []
		if endWord in currLevel:
		    break
	self.buildPath([], prevMap, beginWord, endWord)
	return self.result

sol = Solution()
print sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])

