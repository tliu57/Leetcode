class Solution(object):
	def addBinary(self, a, b):
		if not a:
			return b
		if not b:
			return a
		if a[-1] == '1' and b[-1] == '1':
			return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
		elif a[-1] == '0' and b[-1] == '0':
			return self.addBinary(a[0:-1], b[0:-1]) + '0'
		else:
			return self.addBinary(a[0: -1], b[0: -1]) + '1'


sol = Solution()
a = '11'
b = '1'
print sol.addBinary(a, b)
