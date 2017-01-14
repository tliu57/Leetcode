import math
class Solution(object):
	def numSquares(self, n):
		if self.isSquare(n):
			return 1
		#Legendre's three square theorem
		# n = x^2 + y^2 + z^2 if only if n = 4^a *(8b + 7)
		while n & 3 == 0: # n%4 == 0
			n >>= 2
		if n & 7 == 7: # n%8 == 7
			return 4
		sqroot = int(math.sqrt(n))
		for i in range(1, sqroot+1):
			if self.isSquare(n - i*i):
				return 2
		return 3
		

	def isSquare(self, n):
		sqroot = int(math.sqrt(n))
		for i in range(sqroot+1):
			if i*i == n:
				return True
		return False

sol = Solution()
n = 2
print sol.numSquares(n)
