class Solution(object):
	def lengthOfLongestSubstring(self, s):
		map = {}
		maxLength = 0
		prev = 0
		for i, c in enumerate(s):
			if c in map:
				prev = max(map[c] + 1, prev)
			map[c] = i
			maxLength = max(maxLength, i - prev + 1)
		return maxLength
			
			
s = "abba"
sol = Solution()
# assert sol.lengthOfLongestSubstring(s) == 2
# assert sol.lengthOfLongestSubstring("abcabcbb") == 3
# assert sol.lengthOfLongestSubstring("bbbbb") == 1
# assert sol.lengthOfLongestSubstring("pwwkew") == 3
assert sol.lengthOfLongestSubstring("dvdf") == 3

