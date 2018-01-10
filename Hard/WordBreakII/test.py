class Solution(object):
    def __init__(self):
	self.done = {}
	self.dic = set()

    def wordBreak(self, s, wordDict):
	self.dic = set(wordDict)
	self.done[""] = [""]
	return self.dfs(s)

    def dfs(self, s):
	if s in self.done:
		return self.done[s]
	n = len(s)
	res = []
	for i in range(1, n+1):
	    s1 = s[:i]
	    s2 = s[i:]
	    if s1 in self.dic:
	    	s2_res = self.dfs(s2)
	    	for word in s2_res:
		    if word == "":
		    	res.append(s1)
		    else:
		    	res.append(s1 + " " + word)
	self.done[s] = res
	return res

sol = Solution()
print sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
