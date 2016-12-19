from sets import Set
class Solution(object):
	def diffWaysToCompute(self, input):
		result = list()
		for i in xrange(0, len(input)):
			if input[i] == '+' or input[i] == '-' or input[i] == '*':
				prefix = input[:i]
				postfix = input[i+1:]
				PreResultList = self.diffWaysToCompute(prefix)
				PreResultSet = Set(PreResultList)
				PostResultList = self.diffWaysToCompute(postfix)
				PostResultSet = Set(PostResultList)
				for num1 in PreResultSet:
					for num2 in PostResultSet:
						resNum = 0
						if input[i] == '+':
							resNum = num1 + num2
						if input[i] == '-':
							resNum = num1 - num2
						if input[i] == '*':
							resNum = num1 * num2
						result.append(resNum)
		if len(result) == 0:
			result.append(int(input))
		return list(result)

sol = Solution()
print sol.diffWaysToCompute("2*3-4*5")
