class Solution():
    def lengthOfLongestSubstring(self, s):
	dic = {}
	j = 0
	length = 1
	for i in range(len(s)):
	    if s[i] in dic:
	    	j = max(j, dic[s[i]]+1)
	    dic[s[i]] = i
	    length = max(length, i - j + 1)
	return length

sol = Solution()
print sol.lengthOfLongestSubstring("au")
print sol.lengthOfLongestSubstring("abcabcbb")
print sol.lengthOfLongestSubstring("bbbbb")
print sol.lengthOfLongestSubstring("pwwkew")
