class Solution(object):
    def __init__(self):
	self.string = []

    def licenseKeyFormatting(self, S, K):
	chars = []
	for c in S:
		if c != "-":
			if ord(c)>= ord('0') and ord(c)<= ord('9'):
			    chars.append(c)
			else:
			    chars.append(c.upper())
	if len(chars) % K != 0:
	        index = len(chars) % K
		self.string.extend(chars[0: index])
		self.string.append("-")
		self.formatString(chars, index, K)
	else:
	    	self.formatString(chars, 0, K)
	return "".join(self.string)

    def formatString(self, characters, startingIndex, K):
	i = startingIndex
	while i < len(characters):
	    self.string.extend(characters[i:i+K])
	    i += K
	    if i != len(characters):
	    	self.string.append("-")
	print self.string
	
sol = Solution()
print sol.licenseKeyFormatting("5F3Z-2e-9-w", 4)
sol1 = Solution()
print sol1.licenseKeyFormatting("2-5g-3-J", 2)
