class Solution(object):
	def addBinary(self, a, b):
		indexa = len(a) - 1
		indexb = len(b) - 1
		carry = 0
		sum = ""
		while indexa >= 0 or indexb >= 0:
			numa = int(a[indexa]) if indexa >= 0 else 0
			numb = int(b[indexb]) if indexb >= 0 else 0
			num = numa + numb + carry
			if num % 2 == 1:
				sum = "1" + sum
			else:
				sum = "0" + sum
			carry = num / 2
			indexa -= 1
			indexb -= 1
		sum  = "1" + sum if carry == 1 else sum
		return sum

sol = Solution()
a = "11"
b = "10"
print sol.addBinary(a, b)
