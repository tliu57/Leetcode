class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

	queue = [(beginWord, 1)]
	while queue:
	    currWord, currDist = queue.pop(0)
    	    if currWord == endWord:
	    	return currDist
    	    for i in range(len(currWord)):
		prevPart = currWord[:i]
		postPart = currWord[i+1:]
		for c in "abcdefghijklmnopqrstuvwxyz":
			if c != currWord[i] and prevPart + c + postPart in wordList:
				queue.append((prevPart+c+postPart, currDist+1))
				wordList.remove(prevPart+c+postPart)
	return 0
    		
sol = Solution()
print sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
