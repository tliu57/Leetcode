class Solution():
    def calculate(self, s):
	s = s.strip()
	result = 0
	if len(s) == 0:
		return result
	stack = []
	num = 0
	sign = "+"
	for i in range(len(s)):
	    if s[i].isdigit():
		num = num * 10 + ord(s[i]) - ord('0')
	    if (s[i] != " " and (not s[i].isdigit())) or (i == len(s)-1):
	    	if sign == "+":
	 		stack.append(num)
	    	elif sign == "-":
	 		stack.append(-num)
	    	elif sign == "*":
	 		prev_num = stack.pop()
	 		num = num * prev_num
	 		stack.append(num)
	    	elif sign == "/":
	        	prev_num = stack.pop()
	        	if prev_num < 0:
                        	num = -((-prev_num) / num)
      			else:
      				num = prev_num / num
	                stack.append(num)
	    	num = 0
	    	sign = s[i]
	for num in stack:
	    result += num
	return result


sol = Solution()
#print sol.calculate("3+2*2")
#print sol.calculate("3+2/2")
#print sol.calculate(" 3+5/2")
#print sol.calculate("3/2")
#print sol.calculate("42")
print 3/2
print sol.calculate("14-3/2")
