class Solution(object):
    def strStr(self, haystack, needle):
	if needle == "" and haystack == "":
		return 0
	if needle == "":
		return 0
	if haystack == "":
		return -1
	nexts = self.makeNext(needle)
	print nexts
	j = 0
	i = 0
	while i < len(haystack):

	    if haystack[i] == needle[j]:
	    	i += 1
	    	j += 1
	    if j == len(needle):
		return i-len(needle)
	    elif i < len(haystack) and haystack[i] != needle[j]:
	    	if j != 0:	
	    		j = nexts[j-1]
		else:
		    	i += 1

	return -1

    def makeNext(self, needle):
	length = len(needle)
	nexts = [0 for i in range(len(needle))]
	nexts[0] = 0
	j = 0
	i = 1
	while i < length:
		if needle[i] == needle[j]:
			j += 1
			nexts[i] = j
			i += 1
		else:
			if j != 0:
				j = nexts[j-1]
			else:
				nexts[j] = 0
				i += 1
	return nexts


sol = Solution()
assert sol.strStr("hello", "ll") == 2
assert sol.strStr("aaaaa", "bba") == -1
#print sol.strStr("", "")
#print sol.strStr("a", "")
#print sol.strStr("", "a")
assert sol.strStr("mississippi", "issi") == 1
print sol.strStr("mississippi", "issip")
