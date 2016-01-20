import sys
class Solution(object):
	def minWindow(self, s, t):
		map = {}
		for i in xrange(26):
			map[chr(ord('A') + i)] = 0
		begin = 0
		head = 0
		end = 0
		counter = len(t)
		d = sys.maxint
		for elem in t:
		 	map[elem] += 1
		while end < len(s):
			if map[s[end]] > 0:
				counter -= 1
			map[s[end]] -= 1
			end += 1
			print "for end = %d, map is:"%end, map
			print "---------------------"
			while counter == 0:
				head = begin
				d = end - head
				if map[s[begin]] == 0:
					counter += 1
				map[s[begin]] += 1
				begin += 1
		if d == sys.maxint:
		 	return ""
		return s[head:head+d]
sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print sol.minWindow(s, t)
				
