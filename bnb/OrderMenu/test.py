epsilon = 0.01
class Solution(object):
	def combinationSum(self, candidates, target):
		candidates = sorted(candidates, key = lambda x: x[1])
		res = []
		sub = []
		self.combinationSumHelper(candidates, target, 0, sub, res)
		return res
	
	def combinationSumHelper(self, candidates, target, pos, sub, res):
		if target >= 0 and target < epsilon:
			res.append([elem for elem in sub])
			return
		for i in range(pos, len(candidates)):
			newTarget = target - candidates[i][1]
			if newTarget >= 0:
				sub.append((candidates[i][0], candidates[i][1]))
				self.combinationSumHelper(candidates, newTarget, i, sub, res)
				sub.pop()


menu = [
	("chicken", 1.99),
	("egg", 1.01),
	("lettuce", 1.50),
	("tomato", 0.7)
       ]

sol = Solution()
print sol.combinationSum(menu, 3)
