NOSOL = "No solution"
INFSOL = "Infinite solutions"


class Solution(object):
    def solveEquation(self, equation):
	expressions = equation.split("=")
	if len(expressions) != 2:
		return NOSOLUTION
	A, C = self.evaluateExpression(expressions[0])
	B, D = self.evaluateExpression(expressions[1])
	if A == B and C == D:
		return INFSOL
	elif A == B and C != D:
		return NOSOL
	else:
		val = (D-C) / (A-B)
		return "x=" + str(val)

    def evaluateExpression(self, string):
	res = [0 for i in range(2)]
	import re
	tokens = re.findall("[+-]?[0-9]*x?", string)
	for token in tokens:
	    if token == "+x" or token == "x":
	    	res[0] += 1
	    elif token == "-x":
	    	res[0] -= 1
	    elif "x" in token:
	    	print token
	    	res[0] += int(token[:-1]) 
	    elif len(token) > 0:
	    	res[1] += int(token)
	return res[0], res[1]

sol = Solution()
print sol.solveEquation("x+5-3+x=6+x-2")
print sol.solveEquation("x=x")
print sol.solveEquation("2x+3x-6x=x+2")
print sol.solveEquation("x = x+2")
