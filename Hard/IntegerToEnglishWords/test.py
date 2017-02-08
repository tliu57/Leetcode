class Solution(object):
	UNDER_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
	TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
	THOUSAND = ["", "Thousand", "Million", "Billion"]

	def numberToWords(self, num):
		if num == 0:
			return "Zero"
		res = ""
		i = 0
		while num > 0:
			if num%1000 != 0:
				res = self.helper(num%1000) + self.THOUSAND[i] + " " + res
			num /= 1000
			i += 1
		return res.strip()
	
	def helper(self, num):
		if num == 0:
			return ""
		if num < 20:
			return self.UNDER_TWENTY[num] + " "
		elif num >= 20 and num < 100:
			return self.TENS[num/10] + " " + self.helper(num%10)
		else:
			return self.UNDER_TWENTY[num/100] + " Hundred " + self.helper(num%100)


sol = Solution()
print sol.numberToWords(1234567)
