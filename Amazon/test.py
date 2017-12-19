NOSOL = "No solution"
INFSOL = "Infinite solutions"


class Solution(object):
    def solveEquation(self, equation):
	expressions = equation.split("=")
	if len(expressions) != 2:
		return NOSOLUTION
	ela1 = self.elavuateExpression(expressions[0])
	ela2 = self.elavuateExpression(expressions[1])
	
		
