class Solution(object):
	def countAndSay(self, n):
		s = "1"
		# if n == 1:
		#	return s
		for i in range(2, n+1):
			s = self.count(s)
		return s

	def count(self, s):
		t = ""
		count = 0
		curr = "#"
		for c in s:
			if c != curr:
				if curr != "#":
					t += str(count) + curr
				curr = c
				count = 1
			else:
				count += 1
		t += str(count) + curr
		return t

sol = Solution()
print sol.countAndSay(9)
			
