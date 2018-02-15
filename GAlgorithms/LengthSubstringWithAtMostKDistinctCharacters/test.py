class Solution(object):
    def lengthOfLongestSubsstringKDistinct(self, s, k):
	dic = {}
	i = 0
	num = 0
	res = 0
	for j in range(len(s)):
	    c = s[j]
	    if c not in dic:
	    	dic[c] = 0
	    	num += 1
	    dic[c] += 1
	    while num > k and i < len(s):
		leftchar = s[i]
		if leftchar in dic:
			dic[leftchar] -= 1
			if dic[leftchar] == 0:
				num -= 1
				del dic[leftchar]
		i += 1
	    res = max(res, j - i + 1)
        return res

sol = Solution()
print sol.lengthOfLongestSubsstringKDistinct("eceba", 2)
