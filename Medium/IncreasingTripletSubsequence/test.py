import sys
class Solution(object):
	def increasingTriplet(self, nums):
		c1 = sys.maxint
		c2 = sys.maxint
		for num in nums:
			if num <= c1:
				c1 = num
			elif num <= c2:
				c2 = num
			else:
				return True
		return False

sol = Solution()
print sol.increasingTriplet([1, 2, 3, 4, 5])
print sol.increasingTriplet([1, 2, 2, 1])
