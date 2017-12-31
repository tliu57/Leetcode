import random
import string

class Solution(object):
    def __init__(self):
	self.url2code = {}
	self.code2url = {}
	self.alphabet = string.ascii_letters + '0123456789'

    def encode(self, longURL):
	while longURL not in self.url2code:
		code = ''.join(random.choice(self.alphabet) for _ in range(6))
		if code not in self.code2url:
			self.code2url[code] = longURL
			self.url2code[longURL] = code
	return "http://tinyurl.com/" + self.url2code[longURL]

    def decode(self, shortURL):
	return self.code2url[shortURL[-6:]]

sol = Solution()
print sol.encode("https://leetcode.com/problems/design-tinyurl")

