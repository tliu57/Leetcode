class Solution:
	# @param {string} haystack
	# @param {string} needle
	# @return {integer}
	def strStr(self, haystack, needle):
		
		n = len(needle)

		for i in range(len(haystack) - n - 1):
			if haystack[i: i+n] == needle:
				return i
		return -1
