class Solution(object):
    def calculate(self, s):
	res = 0
	if len(s) == 0:
		return res
	sign = 1
	stack = []
	num = 0
	for i in range(len(s)):
		if s[i].isdigit():
		    num = num * 10 + (ord(s[i]) - ord('0')) 
		elif s[i] == "-":
		    res += sign * num
		    sign = -1
		    num = 0
		elif s[i] == "+":
		    res += sign * num
		    num = 0
		    sign = 1
		elif s[i] == "(":
		    stack.append(res)
		    stack.append(sign)
		    res = 0
		    sign = 1
		elif s[i] == ")":
		    res += sign * num
		    num = 0
		    res *= stack.pop()
		    res += stack.pop()
	if num != 0:
		res += sign * num
	return res

sol = Solution()
print sol.calculate("1 + 1")
print sol.calculate(" 2-1 + 2 ")
print sol.calculate("(1+(4+5+2)-3)+(6+8)")
