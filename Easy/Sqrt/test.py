import sys
class Solution(object):
	def mySqrt(self, x):
		if x == 0:
			return 0
		left = 1
		right = sys.maxint
		while True:
			mid = left + (right - left)/2
			if mid > x/mid:
				right = mid - 1
			else:
				if (mid+1) > x/(mid+1):
					return mid
				left = mid + 1

sol = Solution()
print sol.mySqrt(7)
print sol.mySqrt(16)
