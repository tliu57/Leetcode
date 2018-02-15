class Solution(object):
    def shortestPalindrome(self, s):
	new_s = s
	new_s += "#"
	new_s += s[::-1]
	nexts = self.getnexts(new_s)
	longestPalLen = nexts[-1]
	toBeAdded = s[longestPalLen:]
	return toBeAdded[::-1] + s

    def getnexts(self, s):
	length = len(s)
	nexts = [0 for _ in range(length)]
	j = 0
	i = 1
        while i < length:
                if s[i] == s[j]:
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
print sol.shortestPalindrome("abcd")
print sol.shortestPalindrome("aacecaaa")
