import math
class Solution(object):
	def isPowerOfThree(self, n):
	  """
	  :type n: int
	  :rtype: bool
	  """
	  return n > 0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10


sol = Solution()
n = 3
print sol.isPowerOfThree(n)
