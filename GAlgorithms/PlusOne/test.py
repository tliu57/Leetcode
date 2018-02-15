class Solution():
	def plusOne(self, digits):
		digits[-1] += 1
		for i in range(len(digits)-1, 0, -1):
			if digits[i] != 10:
				continue
			digits[i] -= 10
			digits[i-1] += 1

		if digits[0] >= 10:
			digits[0] -= 10
			digits = [1] + digits
		return digits
	
sol = Solution()
digits = [1, 2, 3, 4]
print sol.plusOne(digits)



for i in range(len(digits)-1, 0 , -1):
	print "i is:", i, "digits[i] is:",digits[i]
