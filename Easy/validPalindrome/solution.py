#! /usr/local/bin/python
import re

#s = "A man, a plan, a canal: Panama"
#s = re.sub("[^A-Za-z0-9]", "", s).lower()
#print s


class Solution:
	# @param {string} s
	# @return {boolean}
	def isPalindrome(self, s):
		s = re.sub("[^A-Za-z0-9]","", s).lower()
		return s == s[::-1]
