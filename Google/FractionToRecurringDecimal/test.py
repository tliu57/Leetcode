class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
	if numerator == 0:
		return "0"
	sign = "-" if (numerator > 0) ^ (denominator > 0) else ""
	abs_num = abs(numerator)
	abs_den = abs(denominator)
	out = ""
	res = abs_num / abs_den
	rem = abs_num % abs_den
	if rem == 0:
		return sign + str(res)
	else:
		out += str(res)
		out += "."
		dictionary = {}
		dictionary[rem] = len(out)
		while rem:
			rem *= 10
			new_res = rem / abs_den
			out += str(new_res)
			new_rem = rem % abs_den
			if new_rem in dictionary:
				index = dictionary[new_rem]
				outlist = list(out)
    				outlist.insert(index, "(")
				outlist.append(")")
				out = "".join(outlist)
				break
			else:
				dictionary[new_rem] = len(out)
			rem = new_rem
		return sign + out

sol = Solution()
#print sol.fractionToDecimal(2, 3)
#print sol.fractionToDecimal(1, 2)
#print sol.fractionToDecimal(1, 7)
print sol.fractionToDecimal(-50, 8)
