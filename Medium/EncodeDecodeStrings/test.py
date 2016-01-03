print "--------test------"
s = "myname"
print s[0:2]
print "--------test------"

class Codec:

	def encode(self, strs):
		"""Encodes a list of strings to a single string.
		:type strs: List[str]
		:rtype: str
		"""
		return ''.join("%d:"%len(s)+s for s in strs)

	def decode(self, s):
		"""Decodes a single string to a list of strings.
		:type s: str
		:rtype: List[str]
		"""
		strs = []
		index = 0
		while index < len(s):
			colon_pos = s.find(':', index)
			index = colon_pos + 1 + int(s[index:colon_pos])
			strs.append(s[colon_pos+1:index])
		return strs

# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = []
strs.append("my")
strs.append("name")
print strs
encoded_str = codec.encode(strs)
print "encoded_str is:", encoded_str
print codec.decode(encoded_str)
