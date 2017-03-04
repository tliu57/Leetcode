import sys
class Solution(object):
	def minWindow(self, s, t):
		need = collections.Counter(t)
        	missing = len(t)
       		i, head, end = 0, 0, 0
        	for j, c in enumerate(s, 1):
                	missing -= need[c] > 0
                	need[c] -= 1
                	if not missing:
                        	while i < j and need[s[i]] < 0 :
                                	need[s[i]] += 1
                                	i += 1
                        	if end == 0 or j - i < end - head:
                                	end = j
                                	head = i
        	return s[head: end]
sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
# print sol.minWindow(s, t)

need = 2
missing = 3

missing -= need > 0
print missing				
