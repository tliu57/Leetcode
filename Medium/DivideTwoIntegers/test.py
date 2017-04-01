class Solution(object):
	def divide(self, dividend, divisor):
		sign = not (dividend > 0)^(divisor > 0)
		dividend = abs(dividend)
		divisor = abs(divisor)
		res = 0
		while dividend >= divisor:
			tmp, i = divisor, 1
			while dividend > tmp << 1:
				tmp <<= 1
				i <<= 1
			dividend -= tmp
			res += i
		res = res if sign else -res
		return min(res, 2147483647)

sol = Solution()
print sol.divide(15, 3)
print sol.divide(24, -7)
print sol.divide(-3, -2)
print sol.divide(-2147483648, -1)
