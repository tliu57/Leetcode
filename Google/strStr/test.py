class Solution(object):
    def strStr(self, haystack, needle):
	index = 0
	while index < len(haystack) - len(needle) + 1:
	    if haystack[index: index+len(needle)] == needle:
	    	return index
	    index += 1
	return -1

sol = Solution()
print sol.strStr("hello", "ll")
print sol.strStr("aaaaa", "bba")
print sol.strStr("", "")
