from sets import Set
from math import pow

class Solution(object):
	def isHappy(self, n):
		used_digit = Set([])
		used_digit.add(n)
		while n!= 1:
			result = 0
			while n != 0:
				result += int(pow(n%10, 2))
				n /= 10
			if result in used_digit:
				return False
			else:
				used_digit.add(result)
				n = result
		return True

sol = Solution()
n = 19
print sol.isHappy(n)
