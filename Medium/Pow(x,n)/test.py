class Solution(object):
	def myPow(self, x, n):
		if n == 0:
			return 1
		elif n < 0:
			x = 1/x
			return self.myPow(x, -n)
		else:
			if n % 2 == 0:
				return self.myPow(x*x, n/2)
		return x*self.myPow(x*x, n/2)

x = 2
n = 5
sol = Solution()
print sol.myPow(2, 5)
print sol.myPow(2, 9)
print sol.myPow(2, 7)
