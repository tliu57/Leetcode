class Solution(object):
	def myPow(self, x, n):
		pow = 1
		if n < 0:
			x = 1/x
			n = -n
		while n:
			if n & 1:
				pow *= x
			x *= x
			n >>= 1
		return pow

sol = Solution()
x = 2
n = 7
print sol.myPow(x, n)
			
			
