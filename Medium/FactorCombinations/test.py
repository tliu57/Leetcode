class Solution(object):
	def getFactors(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		ans = []
		stack = []
		x = 2
		while True:
		    if x > n/x:
		 	if not stack:
		 		return ans
		 	ans.append(stack + [n])
		 	x = stack.pop()
		 	n *= x
		 	x += 1
		    elif n%x == 0:
		    	stack.append(x)
			n /= x
		    else:
		 	x += 1
sol = Solution()
print sol.getFactors(12)
